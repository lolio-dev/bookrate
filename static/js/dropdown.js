class Dropdown {
    constructor(
        triggerId,
        targetId
    ) {
        const targetElement = document.getElementById(targetId);
        const triggerElement = document.getElementById(triggerId);

        triggerElement.addEventListener('click', () => {
            console.log("Hell worldz")
            console.log(targetElement.classList)
            targetElement.classList.toggle('show')
        });
        // TODO: Click outside
        /*window.addEventListener('click', (e) => {
            if (targetElement.classList.contains('show') && !targetElement.contains(e.target)) {
                targetElement.classList.toggle('show')
            }
        });*/
    }
}

const settingsDropdown = new Dropdown("avatar-image", "settings-dropdown")