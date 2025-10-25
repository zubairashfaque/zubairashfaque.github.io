// ===================================
// Theme Toggle
// ===================================
const themeToggle = document.getElementById('theme-toggle');
const html = document.documentElement;

// Check for saved theme preference or default to 'light' mode
const currentTheme = localStorage.getItem('theme') || 'light';
html.setAttribute('data-theme', currentTheme);
updateThemeIcon(currentTheme);

themeToggle.addEventListener('click', () => {
    const theme = html.getAttribute('data-theme');
    const newTheme = theme === 'light' ? 'dark' : 'light';
    html.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
    updateThemeIcon(newTheme);
});

function updateThemeIcon(theme) {
    const icon = themeToggle.querySelector('i');
    icon.className = theme === 'light' ? 'fas fa-moon' : 'fas fa-sun';
}

// ===================================
// Mobile Menu Toggle
// ===================================
const mobileMenuToggle = document.getElementById('mobile-menu-toggle');
const navMenu = document.getElementById('nav-menu');

mobileMenuToggle.addEventListener('click', () => {
    navMenu.classList.toggle('active');
    mobileMenuToggle.classList.toggle('active');
});

// Close mobile menu when clicking on a link
document.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', () => {
        navMenu.classList.remove('active');
        mobileMenuToggle.classList.remove('active');
    });
});

// ===================================
// Smooth Scroll & Active Navigation
// ===================================
const sections = document.querySelectorAll('section[id]');
const navLinks = document.querySelectorAll('.nav-link');

window.addEventListener('scroll', () => {
    let current = '';
    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.clientHeight;
        if (pageYOffset >= sectionTop - 200) {
            current = section.getAttribute('id');
        }
    });

    navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === `#${current}`) {
            link.classList.add('active');
        }
    });
});

// ===================================
// Navbar Scroll Effect
// ===================================
const navbar = document.getElementById('navbar');

window.addEventListener('scroll', () => {
    if (window.scrollY > 100) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
});

// ===================================
// Typing Animation
// ===================================
const typingText = document.querySelector('.typing-text');
const titles = [
    'AI Tech Lead',
    'LLM Architect',
    'Healthcare AI Innovator',
    'Machine Learning Expert',
    'Data Science Consultant'
];

let titleIndex = 0;
let charIndex = 0;
let isDeleting = false;
let typingSpeed = 100;

function typeTitle() {
    const currentTitle = titles[titleIndex];
    
    if (isDeleting) {
        typingText.textContent = currentTitle.substring(0, charIndex - 1);
        charIndex--;
        typingSpeed = 50;
    } else {
        typingText.textContent = currentTitle.substring(0, charIndex + 1);
        charIndex++;
        typingSpeed = 100;
    }

    if (!isDeleting && charIndex === currentTitle.length) {
        isDeleting = true;
        typingSpeed = 2000; // Pause at end
    } else if (isDeleting && charIndex === 0) {
        isDeleting = false;
        titleIndex = (titleIndex + 1) % titles.length;
        typingSpeed = 500; // Pause before next title
    }

    setTimeout(typeTitle, typingSpeed);
}

// Start typing animation
setTimeout(typeTitle, 1000);

// ===================================
// Counter Animation for Stats
// ===================================
const statNumbers = document.querySelectorAll('.stat-number');

const observerOptions = {
    threshold: 0.5,
    rootMargin: '0px'
};

const statObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const target = parseFloat(entry.target.getAttribute('data-target'));
            animateCounter(entry.target, target);
            statObserver.unobserve(entry.target);
        }
    });
}, observerOptions);

statNumbers.forEach(stat => {
    statObserver.observe(stat);
});

function animateCounter(element, target) {
    let current = 0;
    const increment = target / 50;
    const isDecimal = target % 1 !== 0;
    
    const updateCounter = () => {
        current += increment;
        if (current < target) {
            element.textContent = isDecimal ? current.toFixed(1) : Math.ceil(current);
            requestAnimationFrame(updateCounter);
        } else {
            element.textContent = isDecimal ? target.toFixed(1) : target;
        }
    };
    
    updateCounter();
}

// ===================================
// Neural Network Canvas Animation
// ===================================
const canvas = document.getElementById('neural-network');
const ctx = canvas.getContext('2d');

// Set canvas size
function resizeCanvas() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
}

resizeCanvas();
window.addEventListener('resize', resizeCanvas);

// Node class for neural network visualization
class Node {
    constructor(x, y) {
        this.x = x;
        this.y = y;
        this.vx = (Math.random() - 0.5) * 0.5;
        this.vy = (Math.random() - 0.5) * 0.5;
        this.radius = 3;
    }

    update() {
        this.x += this.vx;
        this.y += this.vy;

        if (this.x < 0 || this.x > canvas.width) this.vx *= -1;
        if (this.y < 0 || this.y > canvas.height) this.vy *= -1;
    }

    draw() {
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
        const theme = html.getAttribute('data-theme');
        ctx.fillStyle = theme === 'light' ? 'rgba(30, 64, 175, 0.5)' : 'rgba(6, 182, 212, 0.5)';
        ctx.fill();
    }
}

// Create nodes
const nodes = [];
const nodeCount = 50;

for (let i = 0; i < nodeCount; i++) {
    nodes.push(new Node(
        Math.random() * canvas.width,
        Math.random() * canvas.height
    ));
}

// Animation loop
function animateNetwork() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Update and draw nodes
    nodes.forEach(node => {
        node.update();
        node.draw();
    });

    // Draw connections
    const theme = html.getAttribute('data-theme');
    const lineColor = theme === 'light' ? 'rgba(30, 64, 175, 0.1)' : 'rgba(6, 182, 212, 0.1)';
    
    for (let i = 0; i < nodes.length; i++) {
        for (let j = i + 1; j < nodes.length; j++) {
            const dx = nodes[i].x - nodes[j].x;
            const dy = nodes[i].y - nodes[j].y;
            const distance = Math.sqrt(dx * dx + dy * dy);

            if (distance < 150) {
                ctx.beginPath();
                ctx.moveTo(nodes[i].x, nodes[i].y);
                ctx.lineTo(nodes[j].x, nodes[j].y);
                ctx.strokeStyle = lineColor;
                ctx.lineWidth = 1;
                ctx.stroke();
            }
        }
    }

    requestAnimationFrame(animateNetwork);
}

animateNetwork();

// ===================================
// Project Filtering
// ===================================
const filterButtons = document.querySelectorAll('.filter-btn');
const projectCards = document.querySelectorAll('.project-card');

filterButtons.forEach(button => {
    button.addEventListener('click', () => {
        // Remove active class from all buttons
        filterButtons.forEach(btn => btn.classList.remove('active'));
        // Add active class to clicked button
        button.classList.add('active');

        const filter = button.getAttribute('data-filter');

        projectCards.forEach(card => {
            const categories = card.getAttribute('data-category').split(' ');
            
            if (filter === 'all' || categories.includes(filter)) {
                card.style.display = 'flex';
                card.style.animation = 'fadeInUp 0.5s ease';
            } else {
                card.style.display = 'none';
            }
        });
    });
});

// ===================================
// Scroll Reveal Animation
// ===================================
const revealElements = document.querySelectorAll('.project-card, .pillar-card, .skill-category, .timeline-item, .achievement-card, .cert-card');

const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry, index) => {
        if (entry.isIntersecting) {
            setTimeout(() => {
                entry.target.style.animation = 'fadeInUp 0.6s ease forwards';
            }, index * 100);
            revealObserver.unobserve(entry.target);
        }
    });
}, {
    threshold: 0.1,
    rootMargin: '0px 0px -100px 0px'
});

revealElements.forEach(element => {
    element.style.opacity = '0';
    revealObserver.observe(element);
});

// ===================================
// Skill Progress Bar Animation
// ===================================
const skillBars = document.querySelectorAll('.skill-progress');

const skillObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const width = entry.target.style.width;
            entry.target.style.width = '0';
            setTimeout(() => {
                entry.target.style.width = width;
            }, 100);
            skillObserver.unobserve(entry.target);
        }
    });
}, {
    threshold: 0.5
});

skillBars.forEach(bar => {
    skillObserver.observe(bar);
});

// ===================================
// Project Modal
// ===================================
const modal = document.getElementById('project-modal');
const modalBody = document.getElementById('modal-body');
const modalClose = document.querySelector('.modal-close');

// Project details data
const projectDetails = {
    'agent-nurse': {
        title: 'Agent Nurse Bot',
        company: 'Health Recovery Solutions',
        period: 'Nov 2024 - Mar 2025',
        description: 'Built an advanced Agent Nurse Bot that combines text-to-SQL queries with a sophisticated Retrieval-Augmented Generation (RAG) system. The bot goes beyond simple data retrieval by formulating comprehensive answers using a knowledge base integrated with multiple information sources.',
        challenge: 'Healthcare staff needed instant access to clinical data from databases and knowledge bases simultaneously, without switching between multiple systems or waiting for data lookups.',
        solution: 'Developed an agentic system that intelligently routes queries to either the Redshift database or the RAG knowledge base, then synthesizes responses that combine structured data with contextual information from documents, research papers, and clinical guidelines.',
        impact: [
            '50% reduction in data lookup time',
            'Seamless access to diverse information sources',
            'Context-aware insights for better clinical decision-making',
            'Improved efficiency for clinical staff during critical situations'
        ],
        technologies: ['AWS Bedrock', 'Redshift', 'LangChain', 'RAG', 'Text-to-SQL', 'NLP'],
        features: [
            'Intelligent query routing between SQL and RAG systems',
            'Multi-source knowledge integration',
            'Context-aware response generation',
            'Real-time clinical decision support',
            'Natural language interface for healthcare staff'
        ]
    },
    'readmission': {
        title: 'Readmission Prediction System',
        company: 'Health Recovery Solutions',
        period: 'Nov 2024 - Mar 2025',
        description: 'Engineered a sophisticated predictive analytics model that identifies high-risk patients for hospital readmission, enabling healthcare providers to implement timely interventions and improve patient outcomes.',
        challenge: 'High patient readmission rates were impacting healthcare outcomes and increasing costs. Providers needed a way to proactively identify at-risk patients before they required emergency readmission.',
        solution: 'Developed a real-time machine learning model using XGBoost that analyzes patient data, medical history, and behavioral patterns to calculate individualized risk scores. Deployed the model in an interactive dashboard accessible to healthcare providers.',
        impact: [
            '20% decrease in readmission rates',
            'Timely interventions for high-risk patients',
            'Improved patient outcomes and satisfaction',
            'Significant cost savings for healthcare system'
        ],
        technologies: ['XGBoost', 'Azure ML', 'Python', 'Real-time Analytics', 'Interactive Dashboards'],
        features: [
            'Real-time risk scoring',
            'Interactive monitoring dashboard',
            'Patient risk stratification',
            'Automated alert system for high-risk patients',
            'Historical trend analysis and reporting'
        ]
    },
    'multimodal-rag': {
        title: 'Multimodal RAG System',
        company: 'Health Recovery Solutions',
        period: 'Nov 2024 - Mar 2025',
        description: 'Architected and deployed a cutting-edge Retrieval-Augmented Generation (RAG) solution utilizing AWS Bedrock\'s multimodal capabilities to seamlessly integrate diverse data sources including training videos, research documents, web pages, and internal knowledge bases.',
        challenge: 'Clinical staff were overwhelmed by scattered information across multiple formats and sources, leading to time-consuming searches and potential information gaps during critical decision-making moments.',
        solution: 'Built a unified RAG system powered by AWS Bedrock that ingests, indexes, and retrieves information from multiple modalities. The system understands context across text, video, and images to provide comprehensive, accurate responses.',
        impact: [
            '50% reduction in data lookup times',
            'Enhanced patient care through faster access to information',
            'Streamlined operational workflows',
            'Improved clinical decision-making with comprehensive context'
        ],
        technologies: ['AWS Bedrock', 'Vector Databases', 'Multimodal AI', 'RAG', 'NLP', 'Computer Vision'],
        features: [
            'Multimodal data ingestion (text, video, images)',
            'Semantic search across all content types',
            'Context-aware response generation',
            'Secure, HIPAA-compliant infrastructure',
            'Real-time information retrieval'
        ]
    },
    'churn': {
        title: 'Customer Churn Prevention System',
        company: 'System Limited',
        period: 'Jan 2023 - Oct 2024',
        description: 'Created sophisticated predictive models to forecast customer attrition and recommend data-driven retention actions, significantly improving customer retention and maximizing profitability.',
        challenge: 'High customer attrition rates were affecting revenue stability. The company needed to identify at-risk customers early and understand the factors driving churn to implement effective retention strategies.',
        solution: 'Developed machine learning models using Logistic Regression and Gradient Boosting to predict churn probability for each customer. Built a recommendation engine that suggests personalized retention actions based on customer behavior and risk factors.',
        impact: [
            '15% increase in customer retention',
            '$0.8 million annual profit maximization',
            'Proactive customer engagement strategies',
            'Data-driven decision making for retention'
        ],
        technologies: ['Gradient Boosting', 'Logistic Regression', 'Feature Engineering', 'Python', 'Predictive Analytics'],
        features: [
            'Individual customer churn risk scoring',
            'Behavioral pattern analysis',
            'Automated retention recommendations',
            'Early warning system for at-risk customers',
            'ROI analysis for retention campaigns'
        ]
    },
    'caresage': {
        title: 'CareSage Risk Prediction',
        company: 'Philips Lifeline',
        period: 'Jan 2019 - Dec 2022',
        description: 'Created advanced predictive models using XGBoost and Survival Analysis to anticipate patient risk factors and potential hospitalizations, leading to improved patient outcomes and reduced readmission rates.',
        challenge: 'Healthcare providers needed to anticipate patient health deterioration before it led to emergency hospitalizations, but lacked a systematic way to identify early warning signs across diverse patient populations.',
        solution: 'Developed CareSage, a comprehensive risk stratification system that analyzes patient behavior, medical history, and device usage patterns to predict hospitalization risk. Utilized survival analysis techniques to understand time-to-event patterns.',
        impact: [
            '30% reduction in hospital readmissions',
            'Improved patient outcomes through proactive care',
            'Early intervention opportunities',
            'Enhanced quality of life for high-risk patients'
        ],
        technologies: ['XGBoost', 'Survival Analysis', 'Behavioral Analytics', 'Python', 'Statistical Modeling'],
        features: [
            'Multi-factor risk assessment',
            'Behavioral pattern recognition',
            'Time-to-hospitalization predictions',
            'Patient segmentation and prioritization',
            'Continuous model updating with new data'
        ]
    },
    'fraud': {
        title: 'Fraud Detection System',
        company: 'VEON',
        period: 'Sep 2017 - Jan 2019',
        description: 'Architected and deployed a sophisticated machine learning system to detect grey traffic and fraudulent activities in real-time, significantly reducing revenue loss and protecting company assets.',
        challenge: 'The telecommunications company was experiencing significant revenue loss from grey traffic and fraudulent routing activities that were difficult to detect using traditional rule-based systems.',
        solution: 'Built an ML-powered fraud detection system using XGBoost and anomaly detection algorithms that analyzes traffic patterns in real-time to identify suspicious activities. The system learns from historical fraud cases to continuously improve detection accuracy.',
        impact: [
            '83% detection accuracy',
            'Significant reduction in revenue loss',
            'Real-time fraud prevention',
            'Protection of PKR 1.9 billion in revenue'
        ],
        technologies: ['XGBoost', 'Anomaly Detection', 'Big Data', 'Python', 'Real-time Processing', 'Hadoop'],
        features: [
            'Real-time traffic analysis',
            'Pattern-based fraud detection',
            'Automated alerting system',
            'Historical fraud pattern learning',
            'Scalable big data processing'
        ]
    }
};

function openProjectModal(projectId) {
    const project = projectDetails[projectId];
    if (!project) return;

    modalBody.innerHTML = `
        <div class="modal-project">
            <h2 class="modal-title">${project.title}</h2>
            <div class="modal-meta">
                <span class="modal-company"><i class="fas fa-building"></i> ${project.company}</span>
                <span class="modal-period"><i class="fas fa-calendar"></i> ${project.period}</span>
            </div>
            
            <div class="modal-section">
                <h3><i class="fas fa-info-circle"></i> Overview</h3>
                <p>${project.description}</p>
            </div>

            <div class="modal-section">
                <h3><i class="fas fa-exclamation-triangle"></i> Challenge</h3>
                <p>${project.challenge}</p>
            </div>

            <div class="modal-section">
                <h3><i class="fas fa-lightbulb"></i> Solution</h3>
                <p>${project.solution}</p>
            </div>

            <div class="modal-section">
                <h3><i class="fas fa-chart-line"></i> Impact</h3>
                <ul class="modal-list">
                    ${project.impact.map(item => `<li>${item}</li>`).join('')}
                </ul>
            </div>

            <div class="modal-section">
                <h3><i class="fas fa-cog"></i> Key Features</h3>
                <ul class="modal-list">
                    ${project.features.map(item => `<li>${item}</li>`).join('')}
                </ul>
            </div>

            <div class="modal-section">
                <h3><i class="fas fa-laptop-code"></i> Technologies Used</h3>
                <div class="modal-tech">
                    ${project.technologies.map(tech => `<span class="tech-badge">${tech}</span>`).join('')}
                </div>
            </div>
        </div>
    `;

    modal.style.display = 'block';
    document.body.style.overflow = 'hidden';
}

// Close modal
modalClose.addEventListener('click', closeModal);
modal.addEventListener('click', (e) => {
    if (e.target === modal) {
        closeModal();
    }
});

document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
        closeModal();
    }
});

function closeModal() {
    modal.style.display = 'none';
    document.body.style.overflow = 'auto';
}

// Add modal styles dynamically
const modalStyles = `
    .modal-project {
        max-width: 100%;
    }

    .modal-title {
        font-size: 2rem;
        color: var(--text-primary);
        margin-bottom: 1rem;
    }

    .modal-meta {
        display: flex;
        gap: 2rem;
        margin-bottom: 2rem;
        padding-bottom: 1rem;
        border-bottom: 1px solid var(--border-color);
    }

    .modal-meta span {
        color: var(--text-secondary);
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }

    .modal-meta i {
        color: var(--accent-color);
    }

    .modal-section {
        margin-bottom: 2rem;
    }

    .modal-section h3 {
        font-size: 1.3rem;
        color: var(--text-primary);
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }

    .modal-section h3 i {
        color: var(--accent-color);
    }

    .modal-section p {
        color: var(--text-secondary);
        line-height: 1.8;
    }

    .modal-list {
        list-style: none;
        padding: 0;
    }

    .modal-list li {
        color: var(--text-secondary);
        padding: 0.5rem 0 0.5rem 1.5rem;
        position: relative;
        line-height: 1.7;
    }

    .modal-list li::before {
        content: '▹';
        position: absolute;
        left: 0;
        color: var(--accent-color);
        font-weight: bold;
    }

    .modal-tech {
        display: flex;
        flex-wrap: wrap;
        gap: 0.5rem;
    }

    .tech-badge {
        padding: 0.5rem 1rem;
        background: var(--gradient-primary);
        color: white;
        border-radius: 20px;
        font-size: 0.9rem;
        font-weight: 600;
    }
`;

const styleSheet = document.createElement('style');
styleSheet.textContent = modalStyles;
document.head.appendChild(styleSheet);

// ===================================
// Parallax Effect
// ===================================
window.addEventListener('scroll', () => {
    const scrolled = window.pageYOffset;
    const parallaxElements = document.querySelectorAll('.hero-background');
    
    parallaxElements.forEach(element => {
        const speed = 0.5;
        element.style.transform = `translateY(${scrolled * speed}px)`;
    });
});

// ===================================
// Form Validation (if contact form is added later)
// ===================================
// This can be expanded when a contact form is added

console.log('Portfolio loaded successfully! 🚀');
console.log('Designed and built by Zubair Ashfaque');
