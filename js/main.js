// Add class to navbar on scroll for glassmorphism effect enhancement
window.addEventListener('scroll', () => {
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 50) {
        navbar.style.background = 'rgba(255, 255, 255, 0.95)';
        navbar.style.boxShadow = '0 10px 30px rgba(0,0,0,0.1)';
    } else {
        navbar.style.background = 'rgba(255, 255, 255, 0.85)';
        navbar.style.boxShadow = '0 8px 32px 0 rgba(31, 38, 135, 0.07)';
    }
});

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Mobile menu toggle
const menuToggle = document.querySelector('#mobile-menu');
const navLinks = document.querySelector('#nav-links');

if (menuToggle) {
    menuToggle.addEventListener('click', () => {
        navLinks.classList.toggle('active');
        const icon = menuToggle.querySelector('i');
        if (navLinks.classList.contains('active')) {
            icon.classList.remove('fa-bars');
            icon.classList.add('fa-times');
        } else {
            icon.classList.remove('fa-times');
            icon.classList.add('fa-bars');
        }
    });
}

// Close mobile menu when a link is clicked
document.querySelectorAll('.nav-links a').forEach(link => {
    link.addEventListener('click', () => {
        if (navLinks && navLinks.classList.contains('active')) {
            navLinks.classList.remove('active');
            const icon = menuToggle.querySelector('i');
            icon.classList.remove('fa-times');
            icon.classList.add('fa-bars');
        }
    });
});

// Calculate dynamic years of service and init animations
document.addEventListener('DOMContentLoaded', () => {
    // 1. Dynamic Years
    const yearsOfServiceEl = document.getElementById('years-of-service');
    if (yearsOfServiceEl) {
        const establishmentDate = new Date('2022-08-24');
        const currentDate = new Date();
        let years = currentDate.getFullYear() - establishmentDate.getFullYear();
        const m = currentDate.getMonth() - establishmentDate.getMonth();
        if (m < 0 || (m === 0 && currentDate.getDate() < establishmentDate.getDate())) {
            years--;
        }
        yearsOfServiceEl.setAttribute('data-target', years);
        yearsOfServiceEl.innerText = '0+';
    }

    // Prepare other stats for counting animation
    const stats = document.querySelectorAll('.stat-item h2');
    stats.forEach(stat => {
        if (!stat.hasAttribute('data-target') && stat.id !== 'years-of-service') {
            const val = parseInt(stat.innerText);
            if (!isNaN(val)) {
                stat.setAttribute('data-target', val);
                stat.innerText = '0+';
            }
        }
    });

    // 2. Inject AOS CSS
    const aosCss = document.createElement('link');
    aosCss.rel = 'stylesheet';
    aosCss.href = 'https://unpkg.com/aos@2.3.1/dist/aos.css';
    document.head.appendChild(aosCss);

    // 3. Set AOS attributes before loading JS
    document.querySelectorAll('.branch-card, .file-group, .bank-card, .upi-section').forEach((el, index) => {
        el.setAttribute('data-aos', 'fade-up');
        el.setAttribute('data-aos-delay', (index % 3) * 100);
    });

    document.querySelectorAll('.about-text, .footer-about').forEach(el => {
        el.setAttribute('data-aos', 'fade-right');
    });

    document.querySelectorAll('.vm-card, .footer-links, .footer-contact').forEach((el, index) => {
        el.setAttribute('data-aos', 'fade-left');
        el.setAttribute('data-aos-delay', index * 100);
    });
    
    document.querySelectorAll('.stat-item').forEach((el, index) => {
        el.setAttribute('data-aos', 'zoom-in');
        el.setAttribute('data-aos-delay', index * 150);
    });

    // 4. Inject AOS JS and Initialize
    const aosJs = document.createElement('script');
    aosJs.src = 'https://unpkg.com/aos@2.3.1/dist/aos.js';
    aosJs.onload = () => {
        AOS.init({ duration: 800, once: true, offset: 100 });
        
        // 5. Start Counter Animation on scroll
        let counted = false;
        window.addEventListener('scroll', () => {
            const statsSection = document.querySelector('.impact-section');
            if (!statsSection || counted) return;
            
            const oTop = statsSection.offsetTop - window.innerHeight;
            if (window.scrollY > oTop) {
                stats.forEach(stat => {
                    const updateCount = () => {
                        const target = +stat.getAttribute('data-target');
                        const count = +stat.innerText.replace('+', '');
                        const inc = target / 40; // speed
                        if (count < target) {
                            stat.innerText = Math.ceil(count + inc) + '+';
                            setTimeout(updateCount, 40);
                        } else {
                            stat.innerText = target + '+';
                        }
                    };
                    updateCount();
                });
                counted = true;
            }
        });
        
        // Trigger scroll once in case it's already in view
        window.dispatchEvent(new Event('scroll'));
    };
    document.body.appendChild(aosJs);

    // 6. Automatic Hero Image Slider
    const heroSection = document.querySelector('.hero');
    if (heroSection) {
        const heroImages = [
            'images/sports_awards_team_photo.jpeg',
            'images/sports_awards.jpeg',
            'images/various_parts_of_samiti/श्री_विद्याकुंज_स्पेशल_स्कूल_बंडा.jpeg',
            'images/various_parts_of_samiti/विद्या_छाया_सर्वसुविधायुक्त_सशुल्क_एवं_निःशुल्क_वरिष्ठ_जन_आवास_गृह_बंडा.jpeg'
        ];
        let currentImageIndex = 0;
        
        // Preload images to prevent flickering
        heroImages.forEach(src => {
            const img = new Image();
            img.src = src;
        });

        setInterval(() => {
            currentImageIndex = (currentImageIndex + 1) % heroImages.length;
            heroSection.style.backgroundImage = `linear-gradient(rgba(15, 23, 42, 0.7), rgba(15, 23, 42, 0.8)), url('${heroImages[currentImageIndex]}')`;
        }, 5000); // Change image every 5 seconds
    }
});
