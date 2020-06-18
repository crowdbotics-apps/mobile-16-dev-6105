import { all, takeEvery, take } from "redux-saga/effects";


//@BlueprintReduxSagaImportInsertion
import CalendarView6075Saga from '../features/CalendarView6075/redux/sagas';
import EmailAuth6074Saga from '../features/EmailAuth6074/redux/sagas';
import CalendarSaga from '../features/Calendar/redux/sagas';
import EmailAuthSaga from '../features/EmailAuth/redux/sagas';

function* helloSaga() {
  console.log("Hello from saga!");
}

export function* mainSaga() {
  yield all([
    takeEvery("TEST/ALO", helloSaga),
    // other sagas go here


    //@BlueprintReduxSagaMainInsertion
CalendarView6075Saga,
EmailAuth6074Saga,
CalendarSaga,
EmailAuthSaga,
    
  ]);
}