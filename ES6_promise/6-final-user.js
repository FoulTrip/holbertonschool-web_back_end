import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

async function handleProfileSignup(firstName, lastName, fileName) {
  const promiseOne = {};
  const promiseTwo = {};

  try {
    promiseOne.value = await signUpUser(firstName, lastName);
    promiseOne.status = 'fulfilled';
  } catch (err) {
    promiseOne.value = err.toString();
    promiseOne.status = 'rejected';
  }

  try {
    promiseTwo.value = await uploadPhoto(fileName);
    promiseTwo.status = 'fulfilled';
  } catch (err) {
    promiseTwo.value = err.toString();
    promiseTwo.status = 'rejected';
  }

  return [promiseOne, promiseTwo];
}

export default handleProfileSignup;
