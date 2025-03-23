import time,os
import aixplain
from aixplain.factories import PipelineFactory
import requests
Key="7e253244bde191005f31bf8da48f80b310417abf62f6f2011ac978cc21b730ec"
os.environ["TEAM_API_KEY"] = "7e253244bde191005f31bf8da48f80b310417abf62f6f2011ac978cc21b730ec"

def analyze_symptoms(symptoms):
    if not symptoms:
        raise ValueError("No symptoms provided")

    pipeline = PipelineFactory.get("67d5851202912431287a3fa1")

    try:
        start_response = pipeline.run_async({"Query": symptoms})
        print(start_response)

        poll_url = start_response.get("url")

        # Poll for results until completion
        while True:
            result = pipeline.poll(poll_url)
            if result.get("completed"):
                 data_segments = result.get("data", [])
                 if data_segments:
                        segments = data_segments[0].get("segments", [])
                        for segment in segments:
                            if segment.get("is_url"):
                                response_url = segment.get("response")
                                print("Fetching results from:", response_url)
                                
                                # Fetch data from URL
                                response = requests.get(response_url)
                                if response.status_code == 200:
                                    return response.text  # Return fetched text data
                                else:
                                    raise RuntimeError(f"Failed to fetch data, status code: {response.status_code}")
                    
                        return result  # Return raw result if no URL is found
                 else:
                    time.sleep(5)

    except Exception as e:
        raise RuntimeError(f"Error analyzing symptoms: {str(e)}")
