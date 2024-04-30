import uuid 
from json_manager import JsonManager

class LinkShortener:
    @classmethod
    def get_link_by_id(self,  id: str):
        url_entities = JsonManager.read()
        for url_entity in url_entities:
            if url_entity["id"] == id:
                return url_entity["url"]
        
        raise Exception("Your ID is not found")

    @classmethod
    def shorten(self, url: str):
        data=JsonManager.read()
        exists = False
        for i in data:
            if i['url'] == url:
                exists = True
                print(f"URL Already exists, the short url is: {i['shortened']}")
        if exists == False:
            istrue = True
            while istrue == True:
                unique_id = str(uuid.uuid4())[:1]
                istrue = LinkShortener.check_unique('links.json',unique_id)
            shorturl = f'shorturl.com/{unique_id}'
            new_url_entity = {"id": unique_id, "url": url, "shortened":shorturl}
            url_entities = JsonManager.read()
            url_entities.append(new_url_entity)
            JsonManager.write(url_entities)
            return unique_id
    @classmethod
    def check_unique(self, jsonfile, id):
        data=JsonManager.read(jsonfile)
        for i in data:
            if i['id']==id:
                return True
        return False
print('')
LinkShortener.check_unique('links.json',"044e01b1")





























