<!DOCTYPE html>
<html>
	<head>
		<title>Home</title>
	</head>
	<body>
		<p>Selamat Datang {{username}}</pr>
		<ol>Nama Folder
			<li>{{Dokumen[0]}}</li>
			{%for i in range(0, len)%}
				<ul>{{obj[i]}}</ul>
			{%endfor%}
		</ol>
	</body>
	
</html>