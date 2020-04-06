<!DOCTYPE html>
<html>
<head>
    <title>Compositeurs</title>
    <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
    % include('menubar.tpl')

    <h1>Compositeurs</h1>
    <div class="containerTable">
        <table id="composerTable">
            <tr>
                <th class="clickable" onclick="sortTable(0)">Nom</th>
                <th class="clickable" onclick="sortTable(1)">Naissance</th>
                <th class="clickable" onclick="sortTable(2)">Décès</th>
                <th class="clickable" onclick="sortTable(3)">Nationalité</th>
                <th class="clickable" onclick="sortTable(4)">Style</th>
            </tr>
            % for item in composersArray:
                <tr>
                    <td>{{item['fullname']}}</td>
                    % if item['dateofbirth'] != None:
                        <td>{{item['dateofbirth']}}</td>
                    % else:
                        <td>-</td>
                    % end
                    % if item['dateofdeath'] != None:
                        <td>{{item['dateofdeath']}}</td>
                    % else:
                        <td>-</td>
                    % end
                    <td>{{item['nationality']}}</td>
                    <td>{{item['style']}}</td>
                </tr>
            % end
        </table>
    </div>
    <script src="script.js"></script>
</body>
</html>
