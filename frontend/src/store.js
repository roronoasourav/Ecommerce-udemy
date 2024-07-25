import {legacy_createStore as createStore, combineReducers, applyMiddleware} from 'redux'
import { thunk } from 'redux-thunk'
import {composeWithDevTools} from 'redux-devtools-extension'
import {productListReducers, productDetailsReducer} from './reducers/productReducers'

const reducer = combineReducers({
    productList : productListReducers,
    productDetails : productDetailsReducer,
})

const initialState = {}
// ßconst middleware = [thunk]

const store = createStore(reducer, initialState,
    composeWithDevTools(applyMiddleware(thunk)))

export default store