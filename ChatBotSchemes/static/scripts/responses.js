function getBotResponse() 
{
    var rawText = $("#nameInput").val();
    var userHtml = '<p class="userText"><span>' + rawText + "</span></p>";
    
    $("#nameInput").val("");
    $("#chatbox").append(userHtml);
    document
      .getElementById("userInput")
      .scrollIntoView({ block: "start", behavior: "smooth" });
    $.get("/get", { msg: rawText }).done(function(data) {
      console.log(data)
      var botHtml = '<p class="botText"><span>' + data + "</span></p>";
      $("#chatbox").append(botHtml);
      document
        .getElementById("userInput")
        .scrollIntoView({ block: "start", behavior: "smooth" });
    });
}
  $("#nameInput").keypress(function(e) {
    if (e.which == 13) {
      getBotResponse();
    }
  });