from flask import Flask,request
from db import stores,items
import uuid 
app=Flask(__name__)

#crud
#read all
@app.route('/stores',methods=['GET'])
def get_all_stores():
    return list(stores.values())

@app.route('/items',methods=['GET'])  
def get_all_items():
    return list(items.values())  

#read specific store
@app.route('/stores/<string:store_id>',methods=['GET'])
def get_store(store_id):
    store=stores.get(store_id)
    if store:
        return store,200
    return {'message': f'store with id{store_id}not found'},404  

#read specific item
@app.route('/items/<string:item_id>',methods=['GET'])
def get_item(item_id):
    item=items.get(item_id)
    if item:
        return item,200
    return {'message': f'item with id{item_id}not found'},404    

#create new store
@app.route('/stores/add',methods=['POST'])  
def add_new_store():
    new_store_data=dict(request.get_json())
    # store_id=max(list(stores.keys()))+1 if len(list(stores.keys()))>0 else 1
    store_id=uuid.uuid4().hex
    print(store_id)
    stores[store_id]=new_store_data
    return {'message':'added succ.'},201

#create new item
@app.route('/items/add',methods=['POST'])  
def add_new_item():
    new_item_data=dict(request.get_json())
    if not stores.get(new_item_data['store_id']):
        return {'message':'store not found to add the item in it'},400

    item_id=uuid.uuid4().hex
    print(item_id)
    items[item_id]=new_item_data
    return {'message':'added succ.'},201


#delete item
@app.route('/items/delete/<int:item_id>',methods=['DELETE'])  
def delete_item(item_id):
    try:
        del items[item_id]
    except:
        return{'message':'Item not Found'},404
    return{'message':'Deleted successfully'}, 204   

#delete store
@app.route('/stores/delete/<string:store_id>',methods=['DELETE'])  
def delete_store(store_id):
    try:
        del stores[store_id]
    except:
        return{'message':'Store not Found'},404
    return{'message':'Deleted successfully'}, 204 

#update store
@app.route('/stores/update/<string:store_id>',methods=['PUT'])  
def update_store(store_id):
    updated_store_data=dict(request.get_json())
    if not updated_store_data:
        return{'message':'no updated info.'}, 400
    targeted_store=stores.get(store_id)
    if targeted_store:
        for key in updated_store_data.keys():
            stores[store_id][key]=updated_store_data[key]


        return {'message':'updated succ.'},201


    return{'message':'Store not Found'},404


