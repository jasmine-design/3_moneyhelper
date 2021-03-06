function initializeLiff(myLiffId) {
    liff
        .init({
            liffId: myLiffId
        })
        .then(() => {
            // start to use LIFF's api
            initializeApp();
        })
        .catch((err) => {
            // document.getElementById("liffAppContent").classList.add('hidden');
            // document.getElementById("liffInitErrorMessage").classList.remove('hidden');
        });
}

/**
* Display data generated by invoking LIFF methods
*/
function displayLiffData() {
    // document.getElementById('browserLanguage').textContent = liff.getLanguage();
    // document.getElementById('sdkVersion').textContent = liff.getVersion();
    document.getElementById('isInClient').textContent = liff.isInClient();
    document.getElementById('isLoggedIn').textContent = liff.isLoggedIn();
    document.getElementById('deviceOS').textContent = liff.getOS();
    document.getElementById('lineVersion').textContent = liff.getLineVersion();

    const context = liff.getContext();
    document.getElementById('contextType').textContent = context.type;
}

// login call, only when external browser or LINE's in-app browser is used
document.getElementById('liffLoginButton').addEventListener('click', function () {
    if (!liff.isLoggedIn()) {
        liff.login({ redirectUri: "https://958b4c3a794b.ngrok.io/webpage/liff/liff.html" });
    }
});

// logout call only when external browse
document.getElementById('liffLogoutButton').addEventListener('click', function () {
    if (liff.isLoggedIn()) {
        liff.logout();
        window.location.reload();
    }
});

document.getElementById('getProfile').addEventListener('click', function () {
    if (!liff.isLoggedIn()) {
        alert('To get profile, you need to be logged in. Please tap the "login" button below and try again.');
    } else {
        displayLiffData()
        liff.getProfile()
            .then(profile => {
                document.getElementById('displayName').textContent = profile.displayName;
                document.getElementById('displayPicture').src = profile.pictureUrl;
            })
            .catch((err) => {
                console.log('error', err);
            });
    }
});

document.getElementById('refresh').addEventListener('click', function () {
    window.location.assign("https://liff.line.me/1656056998-RP6bYLXr");
});

document.getElementById('newWindow').addEventListener('click', function () {
    liff.openWindow({
        url: window.location.href
    });
});

function initializeApp() {
    displayLiffData()
}


var myLiffId = "1656056998-RP6bYLXr"
initializeLiff(myLiffId)

