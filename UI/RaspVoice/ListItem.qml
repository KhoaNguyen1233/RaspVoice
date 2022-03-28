import QtQuick 2.12

Item {
    property color cmdcolor: "Red"
    property string cmdName
    property string cmdValue

    Rectangle{
        id: text_container
        height: parent.height
        width: parent.width
        radius: 5
        color: "#FEF3FF"

        Column{
            anchors.fill: parent
            padding: 5
            Text {
                font.pointSize: 15
                font.family: "Futura"
                text: cmdName
            }
            Text {
                font.pointSize: 13
                font.family: "Open Sans"
                text: cmdValue
            }
        }
    }

    ListModel{
        id: testModel
        ListElement{
            mcmdName: "Fans"
            mcmdValue: "1232153"
        }
        ListElement{
            mcmdName: "Diffuser"
            mcmdValue: "1232153"
        }
        ListElement{
            mcmdName: "Light"
            mcmdValue: "1232153"                    
        }
    }
}
