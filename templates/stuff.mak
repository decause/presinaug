<%include file="header.mak"/>
<head>
    <link rel="stylesheet" href="https://bootflat.github.io/bootflat/css/bootflat.css">

</head>

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

<%doc>
<h2>Parts of Speech</h2>
<ul>
    % for name, number, value in pos_legend:
    <li>${name}, ${number}, ${value}</li>
    % endfor
</ul>
</%doc>

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

<%include file="footer.mak"/>
