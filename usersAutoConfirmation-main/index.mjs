export const handler = async (event, context, callback) => {
    try {
      event.response.autoConfirmUser = true;
      event.response.autoVerifyEmail = true;
      callback(null, event);
    } catch (error) {
      console.error(error);
      callback(error);
    }
  };
  
  