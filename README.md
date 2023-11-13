# Newspaper Sentiment Analyzer With Computer Vision

Implementing an app with Streamlit for computer vision using OpenAI Vision API.
The goal is to compute Sentiment Analysis of newspapers pages from images. Note that it is not an OCR problem, the API does not read
the full documents, but only titles and some other highlighted words. The idea is to get a score from -1 to 1, where -1 is extremely
negative and 1 extremely positive, for some user-defined categories taking into account only most catchy titles and words.

## Website Link
[Click here to test it yourself!](https://newspaper-sentiment-analyzer.streamlit.app/) 

## Example

#Input
![Project Image](https://github.com/filopacio/newspaper_sentiment_analyzer/blob/main/data/repubblic.jpg)

#Results

| Infos                     | Values       |
|---------------------------|--------------|
| date                      | 13-11-2023   |
| newspaper                 | la Repubbiica|
| War & Peace               | -0.7         |
| Economic Stability        | -0.5         |
| Technological Trends      | 0            |
| Social Movements          | -0.5         |
| Health & Epidemics        |   0          |
| Political Dynamics        | -0.8         |
| Cultural Shifts           | 0            |
| Global Relations          | -0.3         |
| Scientific Progress       | 0            | 
| Education & Knowledge     | 0            | 
| Religious Landscape       | 0            | 
| Migrations & Immigration  | 0            |
| Government Policies       | -0.8         |
| Natural Disasters         | 0            |
| Local Community Events    | 0            |

```python
{   "date": "13-11-2023",
    "War & Peace": -0.8,
    "Economic Stability": -0.3,
    "Technological Trends": 0.0,
    "Social Movements": 0.0,
    "Health & Epidemics": 0.0,
    "Political Dynamics": -0.5,
    "Cultural Shifts": 0.0,
    "Global Relations": -0.7,
    "Scientific Progress": 0.0,
    "Education & Knowledge": 0.0,
    "Religious Landscape": 0.0,
    "Migrations & Immigration": 0.0,
    "Government Policies": -0.4,
    "Natural Disasters": 0.0,
    "Local Community Events": 0.0
}
```
