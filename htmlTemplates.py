css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://i.ibb.co/cN0nmSj/Screenshot-2023-05-28-at-02-37-21.png" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://scontent.fada1-15.fna.fbcdn.net/v/t39.30808-6/424686259_1660909707772325_1285220508324587896_n.jpg?_nc_cat=105&ccb=1-7&_nc_sid=5f2048&_nc_ohc=jC3Z52vVtZEAX-LaHMp&_nc_ht=scontent.fada1-15.fna&oh=00_AfC6q2IZeYD4WEQCFDtES-E5mBcjnQvqYCf3VUrpKPUxwQ&oe=6611DBA5">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''
