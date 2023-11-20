import { toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

class NotificationService {
  static success(message, position = toast.POSITION.TOP_RIGHT, autoClose = 5000, hideProgressBar = false) {
    toast.success(message, { position, autoClose, hideProgressBar });
  }

  static error(message, position = toast.POSITION.TOP_RIGHT, autoClose = 5000, hideProgressBar = false) {
    toast.error(message, { position, autoClose, hideProgressBar });
  }

  static info(message, position = toast.POSITION.TOP_RIGHT, autoClose = 5000, hideProgressBar = false) {
    toast.info(message, { position, autoClose, hideProgressBar });
  }

  static warn(message, position = toast.POSITION.TOP_RIGHT, autoClose = 5000, hideProgressBar = false) {
    toast.warn(message, { position, autoClose, hideProgressBar });
  }

  static default(message, position = toast.POSITION.TOP_RIGHT, autoClose = 5000, hideProgressBar = false) {
    toast(message, { position, autoClose, hideProgressBar });
  }
}

export default NotificationService;
