# keyoniq-pubmed
A Python tool to parse PubMed XML into Dataframe for query

## Installation Manual
This guide assumes that you use Unix operating systems or the likes (such as WSL Windows Subsystem for Linux).

### Conda
If you use Anaconda or other Conda alternatives like Miniconda or Mamba, you can set up the environment using `keyoniq.yaml` file. Use the following commands:

```
cd keyoniq-pubmed
conda env create -f keyoniq.yaml
conda activate keyoniq
```

Note: if there is a complaint that `conda` command is not found, you may need to `source ~/conda/etc/profile.d/conda.sh`

### Pip
If you don't use Conda, you may install the necessary packages using `requirements.txt` file. Use the following commands:

```
pip3 install -r requirements.txt
```

Note: if you haven't had Pip installed, please do so by `python3 install`

## Quick Use
Once you install the package, you can quickly test the code by running:

```
uvicorn main:app --reload
```

and go to your web browser at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

Make sure you are inside `keyoniq-pubmed` folder and now you can test the code.

1. Click at drop-down for PUT request to initialize the dataframe: you simply need to specify the XML path (e.g., our provided `data/multi-pubmed.xml`).
2. Click at drop-down for GET request to test querying something: you may use simple query like `laser` or more complicated ones including regular expressions like `laser|PMI`, etc.

You may also download your own XML file using [https://pubmed2xl.com/xml/](https://pubmed2xl.com/xml/), since the official PubMed website no longer supports XML export.

## Testing
We have implemented very simple unit tests on our functionality in `test/` folder. To run the test, use the command `python3 -m tests.{$fileName}`, e.g.

```
python3 -m tests.test_data_loader
```
