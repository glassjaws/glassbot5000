from requests_cache import DO_NOT_CACHE, CachedSession
import json

class playerData:

    urls_expire_after = {
        'https://www.playeraudit.com/api/players?s=sarlona': 180,
        'https://www.playeraudit.com/api/players?s=argonnessen': 180,
        'https://www.playeraudit.com/api/players?s=cannith': 180,
        'https://www.playeraudit.com/api/players?s=ghallanda': 180,
        'https://www.playeraudit.com/api/players?s=khyber': 180,
        'https://www.playeraudit.com/api/players?s=orien': 180,
        'https://www.playeraudit.com/api/players?s=thelanis': 180,
        'https://www.playeraudit.com/api/players?s=wayfinder': 180
    }

    session = CachedSession(urls_expire_after=urls_expire_after)

    def __init__(self, characterName, server):
        self.characterName = characterName
        self.server = server

    def request_data(self):
        server = self.server.lower()
        #with self.session.cache_disabled():
        server_data = self.session.get('https://www.playeraudit.com/api/players?s=' + server)
        return server_data.text

    def get_character_info(self):
        characterName = self.characterName.lower()
        server_data = json.loads(self.request_data())
        for players in server_data['Players']:
            if players['Name'].lower() == characterName:
                return(players)

if __name__ == '__main__':
    testing_playerData = playerData('Temnoc', 'Sarlona')
    character = testing_playerData.get_character_info()
    print(character)
    all_classes=""
    for classes in character['Classes']:
        if classes['Name'] != None:
            current_class=(classes['Name'] + ' ' + str(classes['Level']))
            if all_classes == "":
                all_classes=current_class
            else:
                all_classes = ','.join([all_classes, current_class])
    print(all_classes)

    


    

