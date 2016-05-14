def generateHTMLMix(names):

{%for m in names %}

{%for z in m%}
Mint:{{m[1]}}
<div id="tag{{numbers+1}}">
<h4 id="q" style="color:#3f3f3f; margin-top:-2%;">{{z[0]}}</h4>


		
 <div class="row" style="height:50%;">
       
		<div class="shuffledv">
          <div class="tile">
		  <a id="ansA{{numbers+1}}" href="#qwerty" style="a:hover: color:#fff;">
            <img src="http://spectopictures.com/assets/pharMaxology/img/icons/png/A.png" style="width:5%; float:left;">
            <span class="tile-title" style="color:#3f3f3f; font-size:18px;">{{z[1]}}</span><br>
			
		
			</a>
          </div>
       
		
		
		{%for y in z[2] %}
        
          <div class="tile">
		  <a id="ans{{subnumbers}}-{{numbers}}" href="#qwerty" style="a:hover: color:#fff;">
            <img src="http://spectopictures.com/assets/pharMaxology/img/icons/png/A.png" style="width:5%; float: left;">
            <span class="tile-title" style="color:#3f3f3f; font-size:18px;">{{y}}</h4><br>
			
			</a>
          </div>

        {%endfor%}
		
		
	
	
	    </div>

</div>	
</div>
{%endfor%}
{%endfor%}
