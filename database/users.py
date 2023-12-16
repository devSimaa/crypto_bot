from .connect import coll_users

async def get_user(id):
    return coll_users.find_one({"_id":id})

async def add_user(id):
    coll_users.update_one({"$set": {"_id": id}})
    
async def add_favorite_list(id, coin):
    coll_users.update_one({"_id":id},  {"$addToSet":{"list":coin}})

async def get_favorite_list(id):
    return coll_users.find_one({"_id":id},  {"_id": 0})
    