// script.js

function copyToClipboard() {
    const onelinerOutput = document.getElementById('oneliner-output');
    onelinerOutput.select();
    onelinerOutput.setSelectionRange(0, 99999);
    document.execCommand('copy');
    alert('Oneliner copied to clipboard!');
}
