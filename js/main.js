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

// Calculate dynamic years of service
const yearsOfServiceEl = document.getElementById('years-of-service');
if (yearsOfServiceEl) {
    const establishmentDate = new Date('2022-08-24');
    const currentDate = new Date();
    let years = currentDate.getFullYear() - establishmentDate.getFullYear();
    const m = currentDate.getMonth() - establishmentDate.getMonth();
    if (m < 0 || (m === 0 && currentDate.getDate() < establishmentDate.getDate())) {
        years--;
    }
    yearsOfServiceEl.innerText = years + '+';
}
