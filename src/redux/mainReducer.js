import { combineReducers } from "redux";

/**
 * You can import more reducers here
 */


//@BlueprintReduxImportInsertion
import CalendarView6075Reducer from '../features/CalendarView6075/redux/reducers';
import EmailAuth6074Reducer from '../features/EmailAuth6074/redux/reducers';
import CalendarReducer from '../features/Calendar/redux/reducers';
import EmailAuthReducer from '../features/EmailAuth/redux/reducers';

export const combinedReducers = combineReducers({
  blank: (state, action) => {
    if (state == null) state = [];
    return state;
  },


  //@BlueprintReduxCombineInsertion
CalendarView6075: CalendarView6075Reducer,
EmailAuth6074: EmailAuth6074Reducer,
Calendar: CalendarReducer,
EmailAuth: EmailAuthReducer,

});