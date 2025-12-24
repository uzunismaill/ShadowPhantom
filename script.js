document.addEventListener('DOMContentLoaded', () => {
    const videoContainer = document.getElementById('video-container');
    const video = document.getElementById('intro-video');
    const skipBtn = document.getElementById('skip-btn');
    const mainInterface = document.getElementById('main-interface');
    const terminalText = document.getElementById('terminal-text');
    const clockElement = document.getElementById('clock');

    // Transitions from Video to Main Interface
    function transitionToMain() {
        videoContainer.style.opacity = '0';
        setTimeout(() => {
            videoContainer.style.display = 'none';
            mainInterface.classList.remove('hidden');
            startTypingEffect();
            video.pause(); // Ensure video stops resource usage
        }, 1000);
    }

    // Video Events
    video.addEventListener('ended', transitionToMain);
    skipBtn.addEventListener('click', transitionToMain);

    // Clock Functionality
    function updateClock() {
        const now = new Date();
        clockElement.textContent = now.toLocaleTimeString('tr-TR', { hour12: false });
    }
    setInterval(updateClock, 1000);
    updateClock();

    // Typing Effect
    const lines = [
        "Initializing ShadowPhantom Kernel...",
        "Loading modules: [====================] 100%",
        " > crypto_module... OK",
        " > network_sniffer... OK",
        " > brute_force_kit... OK",
        "Establishing secure connection to server...",
        " ...",
        "Connection established (latency: 12ms)",
        "User identity: SHADOW_PHANTOM",
        "Access Level: GOD_MODE",
        "Welcome back, Sir."
    ];

    let lineIndex = 0;
    let charIndex = 0;

    function startTypingEffect() {
        if (lineIndex < lines.length) {
            typeLine(lines[lineIndex]);
        }
    }

    function typeLine(line) {
        const lineElement = document.createElement('div');
        lineElement.classList.add('terminal-line');
        terminalText.appendChild(lineElement);

        let i = 0;
        const typingInterval = setInterval(() => {
            lineElement.textContent += line.charAt(i);
            i++;
            if (i >= line.length) {
                clearInterval(typingInterval);
                lineIndex++;
                setTimeout(startTypingEffect, 200); // Delay between lines
            }
        }, 30); // Typing speed
    }
});
