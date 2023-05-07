# SlackBook

SlackBook is a platform on which people can get in touch with each other. You can form groups/channels here and exchange and discuss any topic here. Texts or pictures can be posted for this. The channels can be public or private, so two people can also chat privately with each other.
The Project can be seen [here](https://slackbook2-0.herokuapp.com/)

- Responsive Mockup
<img src="static/images/responsive-mockup.png" alt="Responsive Mockup">



## User Stories

- As a Site User I can view a list of channel so that I can select one to read the posts.
- As a Site User I can choose between several topics so that I can see different channels refereed to this topic.
- As a Site User I can register an account so that I can comment and join channels.
- As a Site User/Admin I can view comments on an individual post so that I can read the conversation.
- As a Site Admin/User I can create, read, update and delete posts so that I can manage my blog content.
- As a Site User I can leave comments on a post so that I can be involved in the conversation.
- As a Site User I can create, read, update and delete Channels so that I can get in contact with people of same interests.
- As a Site User I can click on a Channel so that I can read the full content.
- As a Site User I can create, update, delete private channels or chats so that I can communicate privately to a person or to a group.
- As a Site User I can upload images so that I can support my statements with pictures and add a personal touch to my avatar
- As a Site User I can search for content so that filter channels or topics


## Features 

- __Header__

    - The header contains the SlackBook logo which is a link to the home webpage. The header also contanisa seachbar and a dropdown menu button with the user image or a default avatar. 
        -  The  dropdown button includes links to the user settings, the user, the user account, to all all channels and categories. If the user is logged in, it also containes the link to the logout page. If the user is not logged in, it contains the link to the log in page.
    - The header has a fixed position and can be seen on all  webpages at the top of the browser window. 
    - On pages where a seachbar makes no scence, it is missing.
    - On small screens the header collapes to the logo and a dropdrown button.
    - The header tells the user the name of the company and clearly guides the user to all the points that interest them. 
     - Header Images
        - Logo
        <img src="static/images/SlackBook-Logo.png" alt="Logo">
        <br>
        - Header large Screen
        <img src="static/images/screenshot-full-header.png" alt="Header1">
        <br>
        - Dropdown menu
        <img src="static/images/screenshot-header-dropdown.png" alt="Dropdown">
        <br>
        - Hamburger menu
        <img src="static/images/screenshot-header-hamburger.png" alt="Hamburger">
        <br>
        - Header small
        <img src="static/images/screenshot-log-out.png" alt="Header2">


- __The Footer__ 

  - The footer section includes links to the relevant social media sites for Slackbook. The links will open to a new tab to allow easy navigation for the user. 
  - The footer is the same on all web pages and fixed.
  - The footer is valuable to the user as it encourages them to keep connected via social media
  - The footer idea and basic code is taken form the **Code-Institute Love-Running-Project** but has been slightly modified.

  - Footer
  <img src="static/images/screenshot-footer.png" alt="Footer">


### The Homepage

 - This section is divided into three parts.

#### Categories and Channel

- The channel categories are displayed on the left side. These can be created by the user. Clicking on it will display all the channels associated with the category the user clicked.
- The channels are displayed below the categories. If no category is clicked, all categories and all channels are displayed. The channel titles of the respective channels are displayed. In addition to the channel titles, the channel hosts are displayed. These are also links that lead to the respective user accounts.

#### User Channels

- In the middle are the channels that the user has joined or which he/she has hosted. The last post of the user is displayed in the channels. Linked here are the channel host and the channel itself.
- If the user is not registered, the request to register can be seen here.

#### Slackbook User

- All SlackBook users are displayed on the right side. These are sorted by the most recent login date and linked to the respective user account. In addition, the most recent post of the respective user is displayed here if they were not posted in a private channels.

    - Landing Page Images
<img src="static/images/screenshot-landing-logged-in.png" alt="Landing">
<br>
<img src="static/images/screenshot-landing-logged-in2.png" alt="Landing2">


### The Channels/Channel Page

- The channels are divided into two parts.

#### Channel-Content

- On the right is the channel title and channel host. Next to it is how long the channel has existed.
- Below is the content of the channel. Also the posts of the user and images (if posted) are displayed here. 
- Also the posts user and when the comment was posted can be seen here.
- The respective user is linked here.

#### Channel-Members
On the right side you can see all members of the channel, who are also linked here.

   - Channel Image
   <img src="static/images/screenshot-channel.png" alt="Channel">


### Categories and Channel Page

- This page shows the same content like in the landing page on the left side. But here it is not filtert. 
- On smaller screens this part ist not shown on the landin page anymore. Instead this page is linked in the header dropdown.
- The channel categories are displayed. These can be created by the user. Clicking on it will display all the channels associated with the category the user clicked.
- The channels are displayed below the categories. If no category is clicked, all categories and all channels are displayed. The channel titles of the respective channels are displayed. In addition to the channel titles, the channel hosts are displayed. These are also links that lead to the respective user accounts.

    - Channel Image
    <img src="static/images/screenshot-categories-channels.png" alt="Channel">



### SlackBook User Page

- This page shows the same content like in the landing page on the right side.
- On smaller screens this part ist not shown on the landin page anymore. Instead this page is linked in the header dropdown.
- All SlackBook users are displayed. These are sorted by the most recent login date and linked to the respective user account. In addition, the most recent post of the respective user is displayed here if they were not posted in a private channels.

  - Active User Image
  <img src="static/images/screenshot-user.png" alt="Active-User">


### User-Settings Page

- Here the user can change some of his personal data. He can change the username, the name and the email address and his avatar. You can log in with your email address.

    - User Settings Image
  <img src="static/images/screenshot-settings.png" alt="User-Settings">


## Create - Update - Delete - Channel

- The create channel, the edit channel and the add member page are rendered by different functions in views.py, but are displayed in the same template. The template looks different depending on which page is being rendered.

### Create-Channel Page

- The user can host their own channel on the Create Channel page. The user has to enter the category (the main topic) and the title of the channel. He also has yet to announce whether it is a private or public channel.
- If it is a private channel, he must then edit the channel and add users manually.
- If the channel is public, every user who posts here will automatically be added as a user.
- Only registered users can create a channel.


### Update-Channel Page

- If the user has hosted a channel, he can then update it. If he clicks "edit" in the channel, he can change the title and category on the page that is being viewed. Also, he can change the channel status from public to private and vice versa. If the channel is private, you'll see a link to "add members" here.

    

### Add-Members Page

- Here you can select individual users and add them to the channel.

    - Create-Channel Image
    <img src="static/images/screenshot-create-channel.png" alt="Create-Channel">

    - Edit-Channel Image
    <img src="static/images/screenshot-edit-channel.png" alt="Edit-Channel">



### Delete Object Page

- The Delete page always looks the same. Posts or channels can be deleted here. To do this, the user first clicks on delete and can then confirm here that the selected object should actually be deleted.
- Alternatively, he can click back and will then be taken back to the previous page.

    - Delete Image
    <img src="static/images/screenshot-delete.png" alt="Create-Channel">

### Account Page

- Different content is displayed on the user account, depending on whether the account owner or a foreign user visits the account.
    - At the very top is the account owner and their user picture, if they have one. Below is a chat function. When a foreign user clicks on it, a private chat is started between the foreign user and the account owner.
    - If this chat already exists, it will be linked here and can be continued.
    - If the account owner visits their own account, all private chats are linked in a drop-down menu instead.
- Below are visible to all, the account owner's hosted channels including the latest posts are displayed. It also shows the channels that the account owner has joined. In addition, the age of the posts and post creators is displayed and linked.

    - User-Account Image
    <img src="static/images/screenshot-user-account.png" alt="User Account">


### Chat Page
- The user gets here when he clicks on "send message" in another account or on the message icon in his own account. Then all the chats that the user either hosted, has, or has been added to will be displayed.
- This shows how long the connection to the other user has existed and the previous chat history.
- A new post can be written and sent underneath.

  - Chat
  <img src="static/images/screenshot-chat.png" alt="Chat">


### 404 Page

- If the user clicks on a link that goes nowhere, they will be directed here.
- An apology and two links will appear. One leads to the previous page, the other leads to the homepage.


## Login - Sign Up - Log Out - Page

- All three pages have been taken over and modified by the Django framework "Allauth".
    - [Django-allauth](https://django-allauth.readthedocs.io/en/latest/)


### The Login Page

  - This page will allow the user to log in to his or her account. If the user has not yet registered, he can do so here. No user can log in without having registered. There is a link to the signup page.
  - The User can log in with email adress and password.

  - Login
  <img src="static/images/screenshot-logIn.png" alt="Log-In">


### The Sign Up Pages

  - In der SignUp Seite muss der Username, und das Passwort angegeben werden. Dieses muss im Nachhinein bestätigt werden. Zusätzlich kann die Emailadresse angegeben werden.
  

  - Sign Up
  <img src="static/images/screenshot-signUp.png" alt="Sign Up">


### The Log Out

  - Here the user can either log out or be directed back to the homepage with a link.

  - Log Out
  <img src="static/images/screenshot-log-out.png" alt="Log-Out">

  - Thank You
  <img src="assets/images/screenshot-thank-you.png" alt="Thank You">




## Features Left to Implement

  - Planned features: 
    - In the future, the user will log in with an e-mail address.
    - Other users will see whether you are online or not.nearby and use the link to further information about her/him.
    - The user will receive a message if he or she has received a message from another user.



## Testing 

- I have manually tested the program in the Code institute Heroku terminal and in my local terminal.by doing the following:
    - I have tested that the website works in different browsers (Chrome and Firefox).
    - I confirm that the website works and looks good on all standard screen sizes. This was tested with the devtools divice toolbar.
    - I confirm that the all forms are working.
    - I confirm that the the user can create, edit and delete channels and posts.
    - Passed the code through the Code institute - PEP8 linter and confirmed that there are no problems

   
 Tested in the Code institute Heroku terminal and in my local terminal.
    CI Python Linter 
    

### Validator Testing

  - CI Python PEP8 Linter 
     - No errors were detected when passing through the CI Python PEP8 Linter.

  - HTML
      - No errors were returned when passing through the official W3C validator.
      - All web pages have been tested.

  - CSS
      - No errors were found when passing through the official (Jigsaw) validator.

  - JavaScipt
      - No errors were found when passing through the JSHint validator.
        

  - Accessibility
      - I confirm that the colors and fonts selected are easy to read and accessible. This was discovered using lighthouse in devtools.
      - All web pages have been tested for desktop and mobil devices.

- HTML Validation
<img src="static/images/screenshot-HTML-val.png" alt="HTML Validation">

- CSS Validation
<img src="static/images/screenshot-css-val.png" alt="CSS Validation">

- JavaScipt Validation
<img src="static/images/screenshot-js-validation.png" alt="JavaScipt Validation">

- Python Validation
<img src="static/images/screenshot-python-val.png" alt="Python Validation">

- Lighthouse
<img src="assets/images/screenshot-lighthouse.png" alt="Lighthouse Desktop">

- user story besed test cases (screenshots):

  - As a visiting user, I can easily understand the main purpose of the website.
      - Slogan and Slideshow
      <img src="assets/images/screenshot-slogan-slideshow.png" alt="Slogan-Slideshow">

  - As a visiting user, I can navigate the website without any problems.
      - Navigation
      <img src="assets/images/screenshot-userstory-test-navigation.png" alt="Navigation">

  - As a visiting user, I will be able to learn about other users and contact them.
      - Info about other user
      <img src="assets/images/screenshot-userstory-test-user-contact.png" alt="Info about other user">

  - As a visiting user, I can easily contact the company service.
      - Company Service
      <img src="assets/images/screenshot-contact.png" alt="Company Service">



### Unfixed Bugs

 - No Bugs are unfixed.
 - But functions that have to be solved better in the future.
    - In the future, the user will log in with an e-mail address.
    - Other users will see whether you are online or not.nearby and use the link to further information about her/him.
    - The user will receive a message if he or she has received a message from another user.



## Deployment

The project was deployed using Code institut's mock for Heroku

    Steps for deployment:
        This repository was cloned.
        A Herroku app was created.
        Added config vars for the secret key, for cloudinary and for the posgresql database.
        The Heroku app was linked to the repository
        Deploy was clicked.

The live link can be found [here](https://slackbook2.herokuapp.com/)


## Credits 

### Content

- Instructions on how to structure full stack projects, how to work with databasis, how to use Django, Postgresql and Cloudinary, Summernote and Allauth are from [Code Institute - I think therefore I Blog](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FST101+2021_T1/courseware/b31493372e764469823578613d11036b/fe4299adcd6743328183aab4e7ec5d13/)
[and](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FST101+2021_T1/courseware/dc049b343a9b474f8d75822c5fda1582/a706dbb65b2d467a84e1bf67266851b1/)
- All icons were taken from [Font Awesome](https://fontawesome.com/)
- Font styles were taken from [Google Fonts](https://fonts.googleapis.com)
- The code of the header dropdown menu is taken from Bootstrap. [Bootstrap](https://getbootstrap.com/docs/4.1/components/navbar/)
- The all HTML structures are from Bootrap. [Bootstrap](https://getbootstrap.com/docs/4.1/layout/grid/)
- Instructions on how to implement links into the footer was taken from [Code Institute - Love Running Project](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+LR101+2021_T1/courseware/4a07c57382724cfda5834497317f24d5/e6d4cda2bc08458ba94d2092be9bad3a/)
- Instructions on how to loop through in the template and count was taken from [Stack Overflow](https://stackoverflow.com/questions/11481499/django-iterate-number-in-for-loop-of-a-template)
- Instructions on how to extend the Django User Model were taken from [Youtube](https://www.youtube.com/watch?v=PtQiiknWUcI&t=9718s)

- Color-Scheme
  <img src="static/images/color-scheme.png" alt="Color Scheme">

### Media

- The Images used on all pages, except the sport-category page and trainer photos on the specific-sport page are from this Open Source site [Pixabay](https://pixabay.com/de/)
- All Images are stored in the Cloudinary platform.
- The Logo was made with [Canva](https://www.canva.com/create/logos/)


### Personal Advice

  - Thank You!
    -  Jubril Akolade
    - All people from my Slack Group!