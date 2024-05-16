from link_shortener import LinkShortener
from fastapi import FastAPI, Request, Response, status
from fastapi.responses import RedirectResponse


app = FastAPI()

@app.get("/api/health_check")
def health_check(r: Request, response: Response):
    # response=requests.Request.get("http://127.0.0.1:8000/api/health_check")
    print(f'The response code is: {response.status_code}')
    print('')
    return(f'{status.HTTP_200_OK}: Healthy')

@app.get("/api/{id}")
def health_check(id: str):
    url = LinkShortener.get_link_by_id(id)
    return RedirectResponse(url)

@app.post("/api/shorten")
def create_url(params: dict):
    url = params["url"]
    id = LinkShortener.shorten(url)
    return {"id": id}



