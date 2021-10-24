# product_IO

## API END POINTS
##### 1 . getProductList
`http://localhost:8000/getProductList`


##### 1 . getProduct [GET]
`http://localhost:8000/getProduct/<int:product_id>`

##### 2 . getProductList [GET]
`http://localhost:8000/getProductList`


##### 3 . createUser [POST]
`http://localhost:8000/createUser`
####### Request:
`{
  "username": "samir",
  "password": "123"
}`

####### Response:
`{
    "username": "samir",
    "token": "67ea0c3129f2a3ee490347b5360a2cc8b838d0c5",
    "id": 2
}`




##### 4 . getProductList [GET]
`http://localhost:8000/getProductList`

##### 4 . createProduct [POST]
`http://localhost:8000/createProduct`

##### 4 . updateProduct [POST]
`http://localhost:8000/updateProduct`

##### 4 . getOrders [GET]
`http://localhost:8000/getOrders`

##### 4 . getUserOrders [GET]
`http://localhost:8000/getUserOrders/<str:username>`

