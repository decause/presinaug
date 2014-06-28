<%include file="header.mak"/>
<head>
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://bootflat.github.io/bootflat/css/bootflat.css">
    <link rel="stylesheet" href="static/css/site.css">
    <link rel="stylesheet" href="static/css/pos.css">

</head>
    <script src="https://bootflat.github.io/bootflat/js/icheck.min.js"></script>
    <script src="https://code.jquery.com/jquery-1.11.0.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.1/js/bootstrap.min.js"></script>
<body>

<h2>StuffList</h2>
<ul>
    <code>${stufflist}</code>
    % for value in stufflist:
        % if value == 'one':
            <li style="color:red">${value}</li>
        % else:
            <li style="color:green">${value}</li>
        % endif
    % endfor
</ul>

<h2>StuffDict</h2>
<ul>
    <code>${stuffdict}</code>
    % for key, value in stuffdict.items():
    <li>${key}: ${value}</li>
    % endfor
</ul>

<h2>StuffTuple</h2>
<ul>
    <code>${stufftuple}</code>
    % for name, number, value in stufftuple:
    <li>${name}, ${number}, ${value}</li>
    % endfor
</ul>

<h2>Parts of Speech</h2>
    % for name, number, value in pos_legend:
        <span class="${value}" data-toggle="tooltip" data-placement="top" title="${number}, ${value}">${name}</span>
    % endfor

<h1>The Raw</h1>
<!-- This is a manual styling, but next will be checking the part of speech,
and then colorizing based on that. Likely not doing it in template-land, but
still a good enough proof-of-concept for a v0.0.1. Also, wtf with not coloring
George? Pobably split problems...-->
<div>
    % for word in raw.split():
        % if word == 'George':
            <span style="color:red">${word} </span>
        % elif word == 'Washington':
            <span style="color:green">${word} </span>
        % elif word == 'Senate':
            <span style="background:yellow">${word} </span>
        % else:
            <span>${word} </span>
        % endif
    % endfor
</div>

<p>${raw}</p>
</body>

<%include file="footer.mak"/>
