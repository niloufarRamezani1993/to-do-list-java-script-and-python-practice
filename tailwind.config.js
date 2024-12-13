/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './*.{html,js}',
    './*.{html,js}',
  ],
  theme:{
     extend: {
        backgroundImage: {
           'leaves': "url('/assets/1.png')"
        
        },
          colors :{
             "silvermine" : "#7C7C7C" ,
            }
         }
      }
  }