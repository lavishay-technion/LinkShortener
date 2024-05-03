from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from link_shortener import LinkShortener

app = FastAPI()

# localhost/health_check
@app.get("/api/health_check")
def healthcheck(r: Request):
    return 'healthy'

@app.get("/api/{id}")
def health_check(id:str):
    url= LinkShortener.get_link_by_id(id)
    return RedirectResponse(url)



@app.post("/shorten")
def create_url(params: dict):
    url=params["url"]
    id=LinkShortener.shorten(url)
    return {'id':id}




















# urls = [
#     "https://walla.co.il",
#     "https://nana.co.il"
# ]

# for url in urls:
#     id = LinkShortener.shorten(url)
#     print(id)