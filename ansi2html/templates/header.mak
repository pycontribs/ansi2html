<style type="text/css">

.body_foreground {
% if dark_bg:
	color : #AAAAAA;
% else:
	color : #000000;
% endif
}

.body_background {
% if dark_bg:
	background-color : #000000;
% else:
	background-color : #AAAAAA;
% endif
}

.body_foreground &gt; .bold,.bold &gt; .body_foreground, body.body_foreground &gt; pre &gt; .bold {
% if dark_bg:
	color : #FFFFFF;
	font-weight : normal;
% else:
	color : #000000;
	font-weight : bold;
% endif
}

.ansi1 { font-weight : bold; }
.ansi3 { font-weight : italic; }
.ansi4 { text-decoration: underline; }
.ansi9 { text-decoration: line-through; }

.ansi30 { color: #000316; }
.ansi31 { color: #aa0000; }
.ansi32 { color: #00aa00; }
.ansi33 { color: #aa5500; }
.ansi34 { color: #0000aa; }
.ansi35 { color: #E850A8; }
.ansi36 { color: #00aaaa; }
.ansi37 { color: #F5F1DE; }

.ansi40 { background-color: #000316; }
.ansi41 { background-color: #aa0000; }
.ansi42 { background-color: #00aa00; }
.ansi43 { background-color: #aa5500; }
.ansi44 { background-color: #0000aa; }
.ansi45 { background-color: #E850A8; }
.ansi46 { background-color: #00aaaa; }
.ansi47 { background-color: #F5F1DE; }

</style>
