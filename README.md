# Developing FAST API to serve models.

As a developer I typically start with a develop a simple program, run, test and deploy and evolve but adding more functionality with end goal in sight.

However, when I started getting into developing solutions for LLM's, it proved a little tough as there seem to be many models being pushed to huggingface and model cards are describing ways to run that particular model.
I was lost for a little while until I ran into [huggingface transformers guiding principals](https://huggingface.co/docs/transformers/philosophy)  and the part that caught my attention was

`On top of those three base classes, the library provides two APIs: pipeline() for `

If I can use pipeline to load and run any model, a wrapper can be written around the pipeline to serve the model. So the journey for kiss_hf (keep it simple stupid - huggingface) began.

Before exploring pipeline I also tried to run [TGI container](https://huggingface.co/docs/text-generation-inference/quicktour) provided by huggingface as containers are being used to run the models. I could not succeed as containers don't seem to work in MacOS.  Using containers also seemed to defeat the purpose of learning from basics.


## Starting Ollama server
For development I had Ollama running on my local machine, outside of devcontainer. To make the ollama models visible in my devcontainer I had to run the model while binding to 0.0.0.0 network interface
```
export OLLAMA_HOST=0.0.0.0:11434
ollama run llama2
```

## Starting fastAPI server
In the devcontainer navigate to circle_ai directory and issue the following command, after the server starts API's can be accessed through a browser
```
uvicorn main:app --host=0.0.0.0 --port=8000

http://localhost:8000/api/docs
```
