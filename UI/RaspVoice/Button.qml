import QtQuick 2.0

Item {
    property string title
    property color buttonColor
    property int buttonState: 0
    property string stage1
    property string stage2
    Rectangle{
        anchors.fill: parent
        color: buttonColor
        radius: 5
        Text {
            id: buttonText
            text: title
            color: "white"
            anchors.centerIn: parent
        }
        MouseArea{
            anchors.fill: parent
            onClicked: {
                if(buttonState == 0){
                    console.log(stage1)
                    buttonState = 1
                    buttonText.text = stage2
                }else{
                    console.log(stage2)
                    buttonState = 0
                    buttonText.text = stage1
                }
            }
        }
    }
}
