
class Utils {
    // Get a unique ID (e.g., for key props in lists)
    static generateUniqueId() {
      return `id_${Math.random().toString(36).substr(2, 9)}`;
    }
  
    // Save data to local storage
    static saveToLocalStorage(key, value) {
      localStorage.setItem(key, JSON.stringify(value));
    }
  
    // Retrieve data from local storage
    static getFromLocalStorage(key) {
      const storedData = localStorage.getItem(key);
      return storedData ? JSON.parse(storedData) : null;
    }
  
    // Remove data from local storage
    static removeFromLocalStorage(key) {
      localStorage.removeItem(key);
    }
  
    // Format a date object as a string
    static formatDate(date) {
      const options = { year: 'numeric', month: 'short', day: 'numeric' };
      return new Date(date).toLocaleDateString(undefined, options);
    }
  
    // Capitalize the first letter of a string
    static capitalizeFirstLetter(str) {
      return str.charAt(0).toUpperCase() + str.slice(1);
    }
  
    // Check if a string is empty or consists only of whitespace
    static isEmptyOrWhitespace(str) {
      return str.trim() === '';
    }
  
    // Debounce function to delay the execution of a function
    static debounce(func, delay) {
      let timeoutId;
      return function (...args) {
        clearTimeout(timeoutId);
        timeoutId = setTimeout(() => {
          func.apply(this, args);
        }, delay);
      };
    }
}
  
export default Utils;
  