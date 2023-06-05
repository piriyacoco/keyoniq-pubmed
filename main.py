from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Dict, List

from scripts import data_loader as dl

app = FastAPI()

class Article(BaseModel):
    pmid: str
    abstract: str

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.put(
    "/articles/", 
    status_code=status.HTTP_201_CREATED,
    summary="Initialize DataFrame",
    description="Create or replace existing Dataframe, given an XML file path"
    )
def initialize_dataframe(xml_path: str) -> Dict[str, List[str]]:
    try:
        tree = dl.parse_tree(xml_path)
        app.state.df = dl.create_df(tree)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail=f"XML file not found at {xml_path}")
    except IOError:
        raise HTTPException(status_code=422, detail=f"corrupted XML file at {xml_path}")
    return {
        "pmid": app.state.df["pmid"].to_list()
    }

@app.get(
    "/articles/", 
    response_model=List[Article],
    summary="Query abstracts",
    description="Get relevant rows from Dataframe based on a query pattern on abstracts"
    )
def query_abstract(query: str) -> List[Dict[str, str]]:
    if not hasattr(app.state, "df"):
        raise HTTPException(status_code=404, detail=f"Dataframe not yet initialized! Use PUT request first!")
    df = dl.query_df(query, app.state.df)
    pmid_list = df["pmid"].to_list()
    abstract_list = df["abstract"].to_list()
    return [{"pmid": pmid_list[idx], "abstract": abstract_list[idx]} for idx in range(len(pmid_list))]