<script src="http://code.jquery.com/jquery-1.10.2.js"></script>
	 <script src="http://code.jquery.com/ui/1.11.4/jquery-ui.js"></script>
     	
<script>
  $( document ).ready(function() {
	  

	  
	  
	   $(".shuffledv").each(function () {
        // Remove all divs within, store in $d
        var $d = $(this).find("div").remove();
        // Sort $d randomnly
        $d.sort(function () { return Math.floor(Math.random() * $d.length); });
        // Append divs within $d to .shuffledv again
        $d.appendTo(this);
    });
	
	
	
	
	   var audioElement = document.createElement('audio');
        audioElement.setAttribute('src', 'http://spectopictures.com/assets/pharMaxology/img/wav/wrong.mp3');
        audioElement.load()

        $.get();

        audioElement.addEventListener("load", function() {
            //audioElement.play();
        }, true);

        $('.play').click(function() {
            audioElement.play();
        });

       var audioElement1 = document.createElement('audio');
        audioElement1.setAttribute('src', 'http://spectopictures.com/assets/pharMaxology/img/wav/good.mp3');
        audioElement1.load()

        $.get();

        audioElement1.addEventListener("load", function() {
            //audioElement.play();
        }, true);

		
		 var audioElement2 = document.createElement('audio');
        audioElement2.setAttribute('src', 'http://spectopictures.com/assets/pharMaxology/img/wav/win.mp3');
        audioElement2.load()

        $.get();

        audioElement2.addEventListener("load", function() {
            //audioElement.play();
        }, true);

     

	  
	  

  $( "#tag1" ).hide();
  $( "#tag2" ).hide();
  $( "#tag3" ).hide();
  $( "#tag4" ).hide();
  $( "#tag5" ).hide();
  $( "#tag6" ).hide();
  $( "#tag7" ).hide();
  $( "#tag8" ).hide();
  $( "#tag9" ).hide();
  $( "#tag10" ).hide();
  
  
  //BAD BAD BAD
  $( "#ansB0" ).click(function() {
   audioElement.play();
	$('#error').show("slow",0).delay(2000).hide("slow",0);

  });
  
   $( "#ansC0" ).click(function() {
   audioElement.play();
	$('#error').show("slow",0).delay(2000).hide("slow",0);

  });
  
  
   $( "#ansD0" ).click(function() {
   audioElement.play();
	$('#error').show("slow",0).delay(2000).hide("slow",0);

  });
  
  
   $( "#ansE0" ).click(function() {
   audioElement.play();
	$('#error').show("slow",0).delay(2000).hide("slow",0);

  });
  
  
  //END END END
  
  
  //BAD BAD BAD
  $( "#ansB1" ).click(function() {
   audioElement.play();
	$('#error').show("slow",0).delay(2000).hide("slow",0);

  });
  
   $( "#ansC1" ).click(function() {
   audioElement.play();
	$('#error').show("slow",0).delay(2000).hide("slow",0);

  });
  
  
   $( "#ansD1" ).click(function() {
   audioElement.play();
	$('#error').show("slow",0).delay(2000).hide("slow",0);

  });
  
  
   $( "#ansE1" ).click(function() {
   audioElement.play();
	$('#error').show("slow",0).delay(2000).hide("slow",0);

  });
  
  
  //END END END
  
  //BAD BAD BAD
  $( "#ansB2" ).click(function() {
   audioElement.play();
	$('#error').show("slow",0).delay(2000).hide("slow",0);

  });
  
   $( "#ansC2" ).click(function() {
   audioElement.play();
	$('#error').show("slow",0).delay(2000).hide("slow",0);

  });
  
  
   $( "#ansD2" ).click(function() {
   audioElement.play();
	$('#error').show("slow",0).delay(2000).hide("slow",0);

  });
  
  
   $( "#ansE2" ).click(function() {
   audioElement.play();
	$('#error').show("slow",0).delay(2000).hide("slow",0);

  });
  
  
  //END END END
  
  
  
  
  //BAD BAD BAD
  $( "#ansB3" ).click(function() {
   audioElement.play();
	$('#error').show("slow",0).delay(2000).hide("slow",0);

  });
  
   $( "#ansC3" ).click(function() {
   audioElement.play();
	$('#error').show("slow",0).delay(2000).hide("slow",0);

  });
  
  
   $( "#ansD3" ).click(function() {
   audioElement.play();
	$('#error').show("slow",0).delay(2000).hide("slow",0);

  });
  
  
   $( "#ansE3" ).click(function() {
   audioElement.play();
	$('#error').show("slow",0).delay(2000).hide("slow",0);

  });
  
  
  //END END END
  
  
   
  
  //BAD BAD BAD
  $( "#ansB4" ).click(function() {
   audioElement.play();
	$('#error').show("slow",0).delay(2000).hide("slow",0);

  });
  
   $( "#ansC4" ).click(function() {
   audioElement.play();
	$('#error').show("slow",0).delay(2000).hide("slow",0);

  });
  
  
   $( "#ansD4" ).click(function() {
   audioElement.play();
	$('#error').show("slow",0).delay(2000).hide("slow",0);

  });
  
  
   $( "#ansE4" ).click(function() {
   audioElement.play();
	$('#error').show("slow",0).delay(2000).hide("slow",0);

  });
  
  
  //END END END
  
  
  //BAD BAD BAD
  $( "#ansB5" ).click(function() {
   audioElement.play();
	$('#error').show("slow",0).delay(2000).hide("slow",0);

  });
  
   $( "#ansC5" ).click(function() {
   audioElement.play();
	$('#error').show("slow",0).delay(2000).hide("slow",0);

  });
  
  
   $( "#ansD5" ).click(function() {
   audioElement.play();
	$('#error').show("slow",0).delay(2000).hide("slow",0);

  });
  
  
   $( "#ansE5" ).click(function() {
   audioElement.play();
	$('#error').show("slow",0).delay(2000).hide("slow",0);

  });
  
  
  //END END END
  
  
  //BAD BAD BAD
  $( "#ansB6" ).click(function() {
   audioElement.play();
	$('#error').show("slow",0).delay(2000).hide("slow",0);

  });
  
   $( "#ansC6" ).click(function() {
   audioElement.play();
	$('#error').show("slow",0).delay(2000).hide("slow",0);

  });
  
  
   $( "#ansD6" ).click(function() {
   audioElement.play();
	$('#error').show("slow",0).delay(2000).hide("slow",0);

  });
  
  
   $( "#ansE6" ).click(function() {
   audioElement.play();
	$('#error').show("slow",0).delay(2000).hide("slow",0);

  });
  
  
  //END END END
  
  //BAD BAD BAD
  $( "#ansB7" ).click(function() {
   audioElement.play();
	$('#error').show("slow",0).delay(2000).hide("slow",0);

  });
  
   $( "#ansC7" ).click(function() {
   audioElement.play();
	$('#error').show("slow",0).delay(2000).hide("slow",0);

  });
  
  
   $( "#ansD7" ).click(function() {
   audioElement.play();
	$('#error').show("slow",0).delay(2000).hide("slow",0);

  });
  
  
   $( "#ansE7" ).click(function() {
   audioElement.play();
	$('#error').show("slow",0).delay(2000).hide("slow",0);

  });
  
  
  //END END END
  
   //BAD BAD BAD
  $( "#ansB8" ).click(function() {
   audioElement.play();
	$('#error').show("slow",0).delay(2000).hide("slow",0);

  });
  
   $( "#ansC8" ).click(function() {
   audioElement.play();
	$('#error').show("slow",0).delay(2000).hide("slow",0);

  });
  
  
   $( "#ansD8" ).click(function() {
   audioElement.play();
	$('#error').show("slow",0).delay(2000).hide("slow",0);

  });
  
  
   $( "#ansE8" ).click(function() {
   audioElement.play();
	$('#error').show("slow",0).delay(2000).hide("slow",0);

  });
  
  
  //END END END
  
   //BAD BAD BAD
  $( "#ansB9" ).click(function() {
   audioElement.play();
	$('#error').show("slow",0).delay(2000).hide("slow",0);

  });
  
   $( "#ansC9" ).click(function() {
   audioElement.play();
	$('#error').show("slow",0).delay(2000).hide("slow",0);

  });
  
  
   $( "#ansD9" ).click(function() {
   audioElement.play();
	$('#error').show("slow",0).delay(2000).hide("slow",0);

  });
  
  
   $( "#ansE9" ).click(function() {
   audioElement.play();
	$('#error').show("slow",0).delay(2000).hide("slow",0);

  });
  
  
  //END END END
  
  	$( "#ansA0" ).click(function() {
		  $("#myBar").css( "width", "10%" );
  $("#percentageT").text("10%");
		audioElement1.play();
		$('#good').show("slow",0).delay(2000).hide("slow",0);
 $( "#tag0" ).hide( "drop", function() {
    // Animation complete.
  }); 
 $( "#tag1" ).show( "slide", function() {
    // Animation complete.
  });
  

});




  	$( "#ansA1" ).click(function() {
		  $("#myBar").css( "width", "20%" );
  $("#percentageT").text("20%");
		audioElement1.play();
		$('#good').show("slow",0).delay(2000).hide("slow",0);
 $( "#tag1" ).hide( "drop", function() {
    // Animation complete.
  }); 
 $( "#tag2" ).show( "slide", function() {
    // Animation complete.
  });
});



    });
	
	</script>
