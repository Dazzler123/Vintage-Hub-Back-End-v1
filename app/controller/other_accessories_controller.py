from fastapi import APIRouter

router = APIRouter()

@router.get('/api/other/v1-create-other')
async def createOtherAccessory():
    # Your logic to get users
    other = [{'id': 1, 'name': 'John'}, {'id': 2, 'name': 'Jane'}]
    return other