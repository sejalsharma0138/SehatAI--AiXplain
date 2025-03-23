import time
import os
os.environ["TEAM_API_KEY"] = "7e253244bde191005f31bf8da48f80b310417abf62f6f2011ac978cc21b730ec"
from aixplain.factories import PipelineFactory

# Load the pipeline using its ID
pipeline = PipelineFactory.get("67d5851202912431287a3fa1")

# Run the pipeline asynchronously with a text input
start_response = pipeline.run_async({"Query": "I have a headache and fever. What should I do?"})

# Polling loop: Wait for the completion of the request
while True:
    result = pipeline.poll(start_response["url"])  # Get the poll URL from start_response
    if result.get("completed"):  # Check if processing is done
        print(result)  # Print the output
        break
    else:
        time.sleep(5) 