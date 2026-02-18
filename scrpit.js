document.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', function(e) {
        // Wir verhindern das normale Springen
        e.preventDefault();
        
        // Die ID aus dem Link holen (z.B. h.6j5maks2n4jn)
        const targetId = this.getAttribute('href').substring(1);
        const targetElement = document.getElementById(targetId);

        if (targetElement) {
            // Alle Inhalte kurz unsichtbar machen
            document.querySelectorAll('#book-content > *').forEach(el => {
                el.style.display = 'none';
            });

            // Nur das gewählte Kapitel und die darauf folgenden Absätze anzeigen
            // bis zur nächsten Überschrift
            let currentNode = targetElement;
            while (currentNode && (currentNode === targetElement || currentNode.tagName !== 'H2')) {
                currentNode.style.display = 'block';
                currentNode = currentNode.nextElementSibling;
                if (!currentNode || currentNode.tagName === 'H2' || currentNode.tagName === 'H1') break;
            }
            
            // Nach oben scrollen für das neue Kapitel
            window.scrollTo(0, 0);
        }
    });
});