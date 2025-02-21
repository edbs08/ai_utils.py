from transformers import pipeline

if __name__=="__main__":
    print(pipeline('sentiment-analysis')('I love you'))