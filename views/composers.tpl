<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
    % include('menubar.tpl')

    <h1>Compositeurs</h1>

    <!-- Button to toggle the form -->
    <button onclick="toggleForm()"><span>Ajouter un compositeur</span></button>
    <div style="display:none" id="form" class="formContainer">
        % include('composerForm.tpl')
    </div>
    <br>
    <hr>
    <br>
    <div class="containerTable">
        <table id="composerTable">
            <tr>
                <th>Nom</th>
                <th>Naissance</th>
                <th>Décès</th>
                <th>Nationalité</th>
                <th>Style</th>
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
