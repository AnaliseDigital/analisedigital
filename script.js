function sendMessage() {
    var userInput = $('#userInput').val().trim();
    if (userInput === '') return;

    $.ajax({
      type: 'POST',
      url: 'backend.php', // PHP script to handle backend logic
      dataType: 'json',
      data: { userInput: userInput },
      success: function(data) {
        displayMessage(userInput, 'user');
        displayMessage(data.response, 'jarvis');
      },
      error: function(xhr, status, error) {
        console.error('Error processing input:', error);
        displayMessage('Error processing input. Please try again.', 'error');
      }
    });

    // Clear input field after sending message
    $('#userInput').val('');
  }

  // Function to display messages in chat interface
  function displayMessage(message, sender) {
    var chatMessages = $('#chatMessages');
    var messageElement = $('<div></div>').addClass('message').addClass(sender).text(message);
    chatMessages.append(messageElement);

    // Scroll to bottom of chat messages
    chatMessages.scrollTop(chatMessages.prop('scrollHeight'));
  }
  