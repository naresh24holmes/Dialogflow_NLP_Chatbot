from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()


@app.route("/", methods=["GET", "POST"])
async def handle_request(request: Request):
    # Retrieve the JSON data from the request
    payload = await request.json()

    # Extract the necessary information from the payload
    intent = payload['queryResult']['intent']['displayName']
    parameters = payload['queryResult']['parameters']
    output_contexts = payload['queryResult']['outputContexts']

    if intent == "track.order - context: ongoing-tracking":
        return JSONResponse(content={
            "fulfillmentText": f"Received == {intent} == in the backend"
        })

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)




