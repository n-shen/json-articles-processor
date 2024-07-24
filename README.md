# Article Json Processor

## Requirements
- python >= 3.6.x

## Usage

### Json Generator

Convert multiple .txt files with title and content into a json object. Accept either group narrative standpoint value or customized narrative standpoint value for each article. Output each to a single .json file under a common folder.

#### Input files
Accept multiple .txt files that:
- Title: the name of the file
- Content: the content in the file

#### Instruction

1. `python3 jsonArticleGen.py`

2. `python3 jsonArticleGen.py [input files path] [output files path]` Remind that for relative path, './' is required!

3. `python3 jsonArticleGen.py [input files path] [output files path] [group narrative value]` Remind that for relative path, './' is required!

### Json Combiner for Articles
 
Convert multiple .json files folders sharing same format into a single json file.

#### Input files
Accept multiple .json files under one or more folders that:

```json
{
    "title": "Title",
    "body": "Body content",
    "true_narrative": 1
}
```

#### Instruction

`python3 jsonCombiner.py`

Enter each folders relative (start with ./) or aboslute path. Press Enter again to end input mod and begin process.
