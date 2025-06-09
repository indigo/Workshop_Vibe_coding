# **Workshop Content Strategy: Vibe Coding**

## **I. Introduction: Deconstructing "Vibe Coding"**

The emergence of powerful Large Language Models (LLMs) capable of generating code has spurred new approaches to software development. One such approach, gaining significant traction, is "Vibe Coding." Understanding its definition, nuances, and implications is crucial for anyone operating at the intersection of technology and creativity.

### **Defining Vibe Coding: Origins, Core Concepts, Key Characteristics**

**Origins:** The term "Vibe Coding" (or vibecoding) was introduced by computer scientist Andrej Karpathy, co-founder of OpenAI and former AI leader at Tesla, in February 2025\.1 Its popularization reflects a perceived tipping point in the capabilities of AI code assistants.3 Karpathy proposed the term to describe a programming approach heavily reliant on LLMs, where the human guides the AI using natural language prompts rather than writing code manually.1 This concept builds upon his earlier assertion in 2023 that "the hottest new programming language is English," signifying the potential for LLMs to translate human intent directly into computer instructions.1 The term quickly gained currency, being listed in the Merriam-Webster Dictionary as "slang & trending" shortly after its introduction and embraced within Silicon Valley discussions.1

**Core Concept:** At its heart, Vibe Coding is a programming *style* or *paradigm* where developers offload much of the code generation, refinement, and debugging process to AI models.1 Instead of meticulously crafting syntax, the developer expresses desired outcomes or features using natural language, either typed or spoken.1 The AI interprets these high-level instructions and produces the corresponding code.3 This represents a fundamental shift in the developer's role – moving from being the direct author of every line of code to acting more like a guide, collaborator, or even a project manager directing a very fast AI engineer.1 Karpathy himself described the experience vividly: "It's not really coding \- I just see things, say things, run things, and copy-paste things, and it mostly works".1

**Key Characteristics:** The Vibe Coding process is typically characterized by several key elements:

* **Natural Language Prompting:** The primary mode of interaction is through natural language descriptions of intent.3  
* **AI as Partner:** The AI functions as a co-developer, pair programmer, or assistant, handling the "heavy lifting" of implementation.3  
* **Iterative Feedback Loop:** Development proceeds through a rapid cycle of prompting the AI, receiving generated code, running or testing the code, providing feedback (often by describing errors or desired changes in natural language), and having the AI revise the code.3 This loop continues until the software behaves as desired.3  
* **Abstraction:** Vibe Coding aims to abstract away the low-level implementation details, allowing the developer to focus on the higher-level goals and ideas.2 Karpathy's phrasing, "forget that the code even exists," captures this ideal, though it also points towards potential risks.1  
* **Acceptance of "Mostly Works":** A defining, and often debated, characteristic is the potential acceptance of code that functions adequately but may not be fully understood or rigorously verified by the human developer.1

This approach signifies the latest step in a long historical trend within software development towards increasing levels of abstraction – from machine code to assembly, to high-level languages, to frameworks, and now potentially to natural language intent.3 The very term "Vibe" suggests a focus on the desired experiential outcome or feeling, perhaps prioritizing intuition and speed over meticulous, low-level precision.6 Its rapid adoption indicates that it resonates with a tangible shift in developer practices, enabled by the increasing power of AI tools like GitHub Copilot, Cursor, Claude, and others.1

### **The Spectrum of AI-Assisted Development: Vibe Coding vs. Responsible AI Use**

While "Vibe Coding" captures a specific, often rapid and intuitive, way of interacting with AI for code generation, it's crucial to distinguish it from the broader spectrum of AI-assisted development. AI researcher Simon Willison provides a critical counterpoint that helps define Vibe Coding more precisely by highlighting what it often entails: a lack of thorough code review and understanding.1

**The Crucial Distinction:** According to Willison, the defining characteristic of Vibe Coding, particularly in the sense Karpathy originally described ("forget that the code even exists"), is **building software with an LLM without necessarily reviewing or fully understanding the code it writes**.7 The user might accept AI suggestions readily, perhaps only copy-pasting error messages back to the AI until the problem appears resolved, without delving into the underlying logic.3

This contrasts sharply with what Willison terms **responsible AI-assisted programming**. In this model, the developer uses the LLM as a powerful tool – perhaps akin to an advanced auto-complete or "typing assistant" 1 – but retains full ownership and responsibility for the code. This involves:

* **Reviewing:** Carefully examining the code generated by the AI.  
* **Testing:** Thoroughly verifying the code's functionality and correctness.  
* **Understanding:** Ensuring comprehension of how the code works, its implications, and potential side effects. Willison advocates a "golden rule": do not commit code to a repository if you cannot explain exactly what it does to someone else.7

**Why Understanding Matters:** The Vibe Coding approach, particularly when review is minimal, carries significant risks. Developers might inadvertently introduce subtle bugs, logical errors, performance bottlenecks, or critical security vulnerabilities by using AI-generated code they don't fully grasp.1 This can lead to unreliable software, difficult maintenance, and accumulating technical debt – essentially taking out a high-interest loan against the codebase's future.4 Professional software engineering demands consideration of numerous factors beyond just functional output, including performance, accessibility, security, maintainability, and cost efficiency.7 An uncritical acceptance of AI code can compromise these aspects. The potential for AI to generate flawed logic, or even fabricate information (like the fake e-commerce reviews mentioned in one case 1), underscores the need for human oversight. An anecdote cited by Ars Technica, where an AI assistant refused to generate code stating the user should "develop the logic yourself," ironically highlights the user's ultimate responsibility.1

**The "YOLO" Aspect and Context:** Some discussions, particularly in informal settings like Reddit threads 2, interpret Vibe Coding with a "You Only Live Once" (YOLO) attitude – simply accepting the AI's output, letting it "rip," and fixing or remaking things if they break.2 While Karpathy acknowledged its potential amusement and utility for "throwaway weekend projects" 1, this casual approach is generally unsuitable for robust, production-level software where reliability and maintainability are paramount.1

The core tension, therefore, lies in the *degree of human oversight and understanding*. This isn't merely a semantic difference but reflects distinct methodologies with different trade-offs. Vibe Coding, in its less reviewed form, prioritizes speed and accessibility, making it potentially well-suited for specific contexts: low-stakes projects, rapid prototyping, creating personal tools ("software for one" 1), learning new languages or frameworks 1, and building developer intuition about LLM capabilities.7 Responsible AI-assisted development prioritizes quality, reliability, and maintainability, essential for professional software engineering, even if it incorporates AI tools extensively.7 Any workshop on Vibe Coding must clearly articulate this spectrum and emphasize the importance of context-appropriate application, equipping attendees with the judgment to use these powerful techniques wisely.

### **Initial Implications: Productivity, Accessibility, and Potential Pitfalls**

The rise of Vibe Coding, enabled by increasingly sophisticated AI, carries significant implications for software development, presenting both exciting opportunities and potential challenges.

**Productivity Boost:** One of the most cited benefits is the potential for a dramatic increase in development speed and productivity.3 By automating the generation of code from natural language prompts, developers can potentially bypass much of the time-consuming process of manual typing, syntax checking, and searching for solutions.6 This allows for faster prototyping, quicker iteration cycles ("build, measure, learn" 4), and reduced time spent on writing boilerplate or repetitive code.4 Some reports suggest significant time savings, such as GitHub Copilot users completing tasks up to 55.8% faster and saving 30-40% on debugging and testing 12, or structured planning with AI reducing bug rates.6

**Democratization & Accessibility:** Vibe Coding significantly lowers the barrier to entry for software creation.1 Individuals with limited or no traditional programming experience can potentially build functional software by describing their needs in plain language.3 This "democratization" empowers a wider range of people – artists, designers, business users, hobbyists – to create custom tools, automate personal tasks, or bring simple software ideas to life without needing extensive training or hiring engineering teams.1 It effectively flattens the initial steep learning curve associated with programming.7

**Potential Pitfalls Revisited:** Despite the advantages, the potential downsides remain significant, particularly when Vibe Coding is practiced without sufficient oversight:

* **Quality and Reliability:** AI-generated code may contain subtle bugs, inefficiencies, or logical errors that are hard to detect without careful review.1 The "mostly works" standard is often insufficient for critical applications.4  
* **Security:** Unverified code can introduce security vulnerabilities, potentially exposing systems and data to risks.1  
* **Maintainability and Technical Debt:** Code generated without adhering to best practices or clear architectural principles can be difficult to understand, modify, and maintain over time, leading to significant technical debt.1  
* **Lack of Understanding & Accountability:** Developers relying heavily on Vibe Coding without review may lack a deep understanding of their own codebase, making debugging and future development challenging.1 This also raises questions about accountability when AI-generated code causes problems.1  
* **Potential for Misuse:** AI could be prompted to generate malicious code or code with unintended harmful consequences, like the example of generating fake reviews.1

These implications paint a picture of Vibe Coding as a powerful but double-edged sword. Its potential to accelerate innovation and broaden participation in software creation is immense. However, realizing these benefits requires navigating the associated risks through critical evaluation, responsible usage, and potentially adapting developer skill sets. The focus may shift from manual coding proficiency towards skills like effective prompt engineering, system architecture design, AI guidance, and rigorous code review.1 The democratization effect could lead to an explosion of personalized tools but also risks flooding digital ecosystems with potentially unreliable software if not managed carefully.1

## **II. The "Vibe": Connecting Vibe Coding to Creative & Technical Domains**

The term "Vibe Coding" inherently suggests a connection to subjective qualities – the feel, aesthetic, or overall experience one aims to achieve. While the *process* involves AI code generation, the *motivation* often stems from creative or experiential goals. This section explores how Vibe Coding relates to specific creative and technical domains like Tech Art, Game Development, and Creative Coding, focusing on the role of aesthetics and "feel."

### **Bridging Vibe Coding and Tech Art**

Technical Artists occupy a unique space, acting as a crucial bridge between artistic vision and technical implementation in fields like game development and animation.14 They require a blend of artistic sensibility (understanding color, form, composition) and technical expertise (scripting, shaders, optimization, pipeline development).15 Vibe Coding presents intriguing possibilities and challenges within this context.

**Relevance and Applications:**

* **Tool Prototyping:** Tech Artists frequently create custom tools and scripts to streamline workflows for artists using Digital Content Creation (DCC) software (e.g., Maya, Blender, Houdini) or game engines (e.g., Unity, Unreal Engine).15 Vibe Coding could significantly accelerate the prototyping phase for these tools, allowing Tech Artists to quickly generate initial script structures (e.g., in Python for Maya/Blender, or using editor scripting APIs) based on natural language descriptions of the desired functionality.17 This speeds up the process of automating repetitive tasks or creating bespoke solutions for specific artistic needs.15  
* **Shader and VFX Experimentation:** Developing shaders (e.g., using HLSL, GLSL) and visual effects (VFX) is a core Tech Art responsibility, often involving iterative experimentation to achieve a specific look or behavior.15 Vibe Coding could assist in generating shader code snippets, exploring different lighting interactions, or prototyping simple particle system behaviors, allowing for faster visual iteration.21  
* **Procedural Content Exploration:** Tech Artists are often involved in procedural generation techniques for creating assets or environments.19 Vibe Coding could be used to quickly sketch out procedural logic, generate variations of simple procedural models, or experiment with algorithms before committing to a full implementation.28  
* **Learning New Technologies:** The field requires continuous learning of new software, APIs, and scripting languages.1 Vibe Coding can serve as a learning accelerator, helping Tech Artists get started with unfamiliar technologies by generating example code or translating concepts into practice.1

Challenges:  
The primary challenge lies in the potential conflict between the "mostly works" nature of pure Vibe Coding and the high demands for precision, performance optimization, and stability often required in Tech Art.14 Tools integrated into production pipelines must be robust and efficient. Shaders and effects need to perform well across target hardware, especially in real-time applications like games.14 Therefore, while Vibe Coding can be a powerful starting point, the generated code typically requires rigorous review, optimization, and refinement using traditional development practices before being used in production.7  
Vibe Coding appears most valuable for Tech Artists as an *ideation, prototyping, and learning tool*. It allows for rapid exploration of technical solutions to artistic problems, facilitating experimentation without the initial burden of complex manual coding. However, for final, production-ready tools, shaders, or pipeline components, it serves best as a starting point or assistant, necessitating subsequent expert review and refinement to meet the stringent requirements of performance and reliability inherent in the Tech Art discipline. Focusing workshop content on Vibe Coding for tech-art tool prototyping leverages Richard Rispoli's background and addresses a common need within the field.15

### **Vibe Coding in Game Development**

Game development is an inherently iterative process, involving the complex interplay of mechanics, narrative, aesthetics, user experience, and technology.33 The industry often operates under tight deadlines and requires rapid prototyping to find engaging gameplay ("find the fun") early in the development cycle.34 Vibe Coding's emphasis on speed aligns well with these needs, particularly in the initial stages.

**Relevance and Applications:**

* **Rapid Prototyping:** Vibe Coding is exceptionally well-suited for quickly building functional prototypes to test core game mechanics, control schemes, or novel gameplay ideas.4 This allows developers and designers to get playable versions running much faster than traditional methods, facilitating early feedback and iteration, fitting well with Agile and Lean development philosophies like the "build, measure, learn" cycle.4  
* **Concept Validation:** Simple versions of features or systems can be generated quickly using Vibe Coding for internal review or early user testing, helping teams validate concepts before investing significant development resources.4  
* **Exploring "Game Feel":** Achieving the right "game feel" – the tactile, satisfying quality of interaction encompassing responsiveness, intuitiveness, and viscerality 39 – often involves extensive tuning and experimentation. Vibe Coding could accelerate this process by allowing developers to rapidly generate and test variations in code related to player movement (e.g., jump physics, acceleration), input handling (e.g., input buffering, coyote time 40), collision responses, or feedback mechanisms (e.g., screen shake, particle effects, hit pauses 39).  
* **Generating Placeholder Content:** In early development stages, Vibe Coding can be used to generate simple placeholder scripts for non-player character (NPC) behaviors, basic UI interactions, event triggers, or simple level logic, allowing other aspects of the game to proceed while more robust systems are developed.  
* **Learning New Engines/Frameworks:** Game development often involves working with complex engines like Unity or Unreal Engine.15 Vibe Coding can help developers get acquainted with unfamiliar engine APIs or scripting languages (like C\# for Unity or Blueprints/C++ for Unreal) by generating initial code examples for common tasks.1

Challenges:  
The critical requirements for performance, stability, memory management, and maintainability in commercial games present significant hurdles for relying solely on Vibe Coding for production code.1 AI-generated code might be inefficient, contain hard-to-find bugs, or lack the architectural soundness needed for large, complex game systems. The potential for introducing technical debt is high if unreviewed code makes its way into the main codebase.4  
The primary value of Vibe Coding in game development appears concentrated in the pre-production, prototyping, and experimentation phases, where the speed of iteration outweighs the need for production-level robustness.4 It offers a powerful way to explore design space, test ideas, and tune subjective elements like game feel more rapidly. For production code, a **hybrid approach** seems most practical: using Vibe Coding for initial drafts, prototypes, or specific components, followed by rigorous review, refactoring, optimization, and integration using established software engineering practices.4 This balanced strategy captures the speed benefits while mitigating the risks associated with unverified AI-generated code.

### **Vibe Coding and Creative Coding/Generative Art**

Creative coding utilizes programming as a medium for artistic expression, exploration, and creating aesthetic experiences, often focusing on visuals, interactivity, and generative processes.44 Generative art, a subset of this, employs algorithms, often incorporating randomness or computational systems, to produce artworks.47 Vibe Coding offers a potentially transformative tool for practitioners in these fields.

**Relevance and Applications:**

* **Rapid Idea Sketching:** Creative coders can use Vibe Coding to quickly translate visual concepts or algorithmic ideas into initial code sketches, using popular environments like p5.js, Processing, or web-based libraries like three.js.8 This lowers the activation energy needed to start a new piece.  
* **Exploring Algorithmic Variations:** Generative systems often rely on tweaking parameters and rules. Vibe Coding allows artists to prompt the AI for variations in algorithms, generating different visual outputs or behaviors without manually rewriting large code sections.8  
* **Adding Interactivity:** Implementing user interaction (e.g., responding to mouse movements, keyboard input, webcam data, sound) can be tedious. Vibe Coding can quickly scaffold the necessary code structures for making creative projects interactive.8  
* **Learning Creative Coding Libraries/Frameworks:** The diverse ecosystem of creative coding tools (p5.js, Processing, openFrameworks, TouchDesigner, three.js, etc.) can be daunting.50 Vibe Coding can act as a guide, generating example code and helping users understand how to use specific functions or libraries.1  
* **Overcoming Creative Blocks:** The "blank page problem" is common in creative pursuits.68 AI prompts can generate initial structures, patterns, or starting points, helping artists overcome inertia and begin the creative process.68

Challenges:  
A key consideration is the nature of creativity and authorship when using AI. While Vibe Coding can generate complex and aesthetically interesting outputs, questions arise about whether this constitutes genuine novelty or merely sophisticated recombination of the AI's training data.54 The "happy accidents" and serendipitous discoveries that often arise from deep engagement with code in traditional creative coding 48 might be replaced by the AI's own stochastic processes, potentially altering the artist's relationship with the medium. Maintaining artistic intent and ensuring the output aligns with the creator's vision requires careful guidance and curation of the AI's results.48  
Vibe Coding stands to significantly lower the technical barrier for entry into creative coding and generative art, making these practices accessible to a broader range of artists and designers who might be less comfortable with traditional programming.49 The role of the creative coder may evolve towards that of a "conductor" 48, "curator," or "collaborator" with the AI 55, focusing more on high-level concepts, prompt crafting, system design, and critical selection of outcomes, rather than line-by-line implementation.8 This introduces a fascinating philosophical tension regarding intentionality, authorship, and originality in the age of generative AI 54, a topic ripe for discussion in a workshop setting.

### **The Role of Aesthetics and "Feel"**

The very name "Vibe Coding" points towards a focus on achieving a specific subjective quality – an aesthetic, an atmosphere, an emotional response, or a particular user experience "feel." While the technique is about AI-driven code generation, the underlying motivation is often rooted in these less tangible, experiential goals.

**Connecting Concepts:** Achieving the right "vibe" is central to many creative technology fields. Aesthetics – encompassing visual style, sound design, narrative tone, and overall presentation – are critical for player engagement, user satisfaction, and conveying artistic intent in games, interactive media, and software interfaces.14 Similarly, "game feel" relates to the quality of interaction, responsiveness, and perceived physicality that makes gameplay satisfying.39 Concepts like "Aesthetic Coding" 44 and "Expressive Coding" 45 further emphasize the use of code for achieving aesthetic and expressive outcomes.

**Vibe Coding for Aesthetic Exploration:** Vibe Coding can be framed as a tool specifically suited for exploring the aesthetic and experiential dimensions of a project rapidly:

* **Visual Style Iteration:** Prompting AI to generate code variations for different visual styles – perhaps experimenting with color palettes 64, applying different shader effects (like toon shading 21), or generating different UI layouts – allows for quick visual prototyping.8  
* **UI/UX Prototyping:** Quickly building and testing different UI interactions, animations, or user flows helps evaluate their "feel" and usability early in the design process.34  
* **Game Feel Tuning:** As mentioned previously, Vibe Coding can generate variations in code controlling movement, input response, and feedback effects, accelerating the iterative process of tuning game feel.39

**Affective Computing Link:** The concept of "vibe" also resonates with Affective Computing, the field dedicated to systems that can recognize, interpret, process, and even simulate human emotions.78 While speculative, one could envision using Vibe Coding to prototype systems designed to *respond* to user emotional states (e.g., changing game difficulty based on detected stress 80, adapting educational content based on frustration 78, or altering visual aesthetics based on mood). Furthermore, future AI systems might even be capable of *analyzing* the likely "vibe" or emotional impact of the experiences they help generate 84, creating a feedback loop within the Vibe Coding process itself.

Ultimately, while Vibe Coding describes a *method* (AI-driven code generation), its purpose is frequently tied to achieving a desired *outcome* related to aesthetics, user experience, or emotional resonance. It provides a potentially faster path to exploring the "look and feel" of a digital creation, allowing artists and designers to iterate on the subjective qualities of their work more efficiently. The connection to Affective Computing hints at future possibilities where AI not only helps create the "vibe" but also understands and interacts with it on an emotional level.

## **III. Understanding the Audience: Tailoring the Vibe**

A successful workshop requires understanding the diverse backgrounds, goals, and challenges of its potential attendees. Tailoring the content and activities of the "Vibe Coding" workshop to resonate with specific professional profiles will significantly enhance engagement and learning outcomes. Based on the research, we can profile several key groups:

**Profile: Tech Artists**

* **Context/Goals:** Tech Artists operate at the crucial intersection of art and programming. Their primary goals involve creating and maintaining art pipelines, developing tools to empower artists, implementing shaders and visual effects (VFX), optimizing game assets for performance, and ensuring the artistic vision is realized within technical limitations.14 They often need to adapt to and learn new software, scripting languages, and APIs.1  
* **Challenges:** A constant challenge is balancing aesthetic quality with performance constraints, especially on diverse hardware like mobile devices.14 Managing complex production pipelines, automating repetitive manual tasks for efficiency, and staying current with rapidly evolving technologies are also key difficulties.15  
* **Vibe Coding Resonance:** The potential for Vibe Coding to rapidly prototype tools 15, quickly experiment with shader code or VFX concepts 15, automate simple pipeline tasks 17, and accelerate the learning of new scripting languages or engine APIs 1 makes it highly relevant.  
* **Workshop Focus:** Hands-on exercises focused on prompting AI to generate simple scripts for DCC applications (e.g., Maya/Blender Python), basic shader code stubs (e.g., GLSL/HLSL fragments for Unity/Unreal), or simple procedural logic. Case studies demonstrating AI assistance in tech art workflows would be beneficial.

**Profile: Game Developers (Programmers, Designers)**

* **Context/Goals:** Game Developers aim to create engaging and immersive gameplay experiences. This involves designing and implementing core mechanics, building game worlds, optimizing performance across target platforms, iterating rapidly on designs, and balancing intricate systems of rules, aesthetics, and narrative.33  
* **Challenges:** Common challenges include managing project scope and meeting deadlines 34, overcoming technical hurdles in implementation 34, efficiently debugging complex systems 34, balancing feature development with available time and resources 34, and achieving the desired subjective "game feel".39  
* **Vibe Coding Resonance:** The alignment with Agile/Lean principles 4 and the potential for rapid prototyping of mechanics 4 are major draws. Vibe Coding can help validate concepts quickly 4, allow for faster exploration of parameters affecting game feel 39, generate placeholder code for early builds 4, and speed up the process of learning new game engines or APIs.1  
* **Workshop Focus:** Exercises centered on prompting for core gameplay elements (e.g., player movement scripts, simple interaction systems), generating code variations to tune "game feel" parameters (like jump height/gravity, input buffering 40), creating basic AI agent behaviors, or scaffolding UI logic. Discussion should cover the practicalities of transitioning from Vibe-Coded prototypes to production code.

**Profile: UI/UX Designers (especially in Games/Interactive Media)**

* **Context/Goals:** UI/UX Designers focus on creating intuitive, accessible, and engaging user interfaces and experiences. In games and interactive media, this involves designing menus, HUDs, control schemes, onboarding processes, and ensuring aesthetic consistency while supporting gameplay.35 They aim for high learnability, memorability, and user satisfaction.35  
* **Challenges:** Balancing visual appeal (aesthetics) with clarity and functionality is key.33 Designing and implementing complex interactions 35, effectively testing user experience over potentially long gameplay durations 35, and ensuring consistency across different platforms or screen sizes are common hurdles.74 Often, designers may lack the coding skills to directly prototype their interactive ideas.6  
* **Vibe Coding Resonance:** Vibe Coding offers a powerful way to rapidly prototype interactive UI elements, flows, and animations without requiring deep coding expertise.6 Designers can potentially test different interaction models, generate code for various visual states, and explore aesthetic variations more quickly 75, bridging the gap between design mockups and functional prototypes.  
* **Workshop Focus:** Exercises involving prompting for UI component generation (e.g., interactive buttons, dynamic menus), simple animation code (fades, transitions, basic motion), or exploring different layout variations based on descriptions. Discussions should emphasize how Vibe Coding can empower designers in the prototyping phase.

**Profile: Creative Coders / Generative Artists**

* **Context/Goals:** This group uses code primarily as a medium for artistic expression, exploration, and experimentation.44 They create generative art, interactive installations, data visualizations, and other digital experiences using tools like Processing, p5.js, openFrameworks, or TouchDesigner.50  
* **Challenges:** Common creative challenges include overcoming the initial "blank page" syndrome 68, translating abstract ideas into concrete code 68, getting stuck during the development process 68, encountering technical barriers that hinder creative flow 49, and managing the complexity of generative systems.  
* **Vibe Coding Resonance:** Vibe Coding can significantly accelerate the sketching of ideas 8, facilitate rapid exploration of algorithmic variations 8, generate boilerplate code for common creative coding frameworks 8, simplify the addition of interactivity 8, and aid in learning new libraries or techniques.1 There's also interest in the potential of AI as a creative collaborator.52  
* **Workshop Focus:** Hands-on exercises using accessible environments like p5.js or Processing. Prompting for generative visual patterns 8, simple animations, or interactive elements responding to user input. Exploring prompt engineering specifically for achieving desired aesthetic outcomes. Facilitating discussions on AI's role in creativity, authorship, and the artistic process.54

**Profile: AI Practitioners / ML Developers**

* **Context/Goals:** These individuals are involved in building, training, and deploying AI models.13 They are interested in understanding the capabilities and limitations of AI, exploring novel applications, and refining AI development workflows.90 Key areas of focus include prompt engineering, model trustworthiness, safety, ethics, and data governance.71  
* **Challenges:** Ensuring the reliability, safety, and robustness of AI systems.90 Managing data privacy and governance.90 Achieving transparency and explainability in AI models.90 Mitigating bias and ensuring fairness.90 Addressing the complex ethical considerations surrounding AI development and deployment.55 Bridging the gap between AI research and practical, real-world applications.  
* **Vibe Coding Resonance:** Interest lies in understanding Vibe Coding as a novel human-AI interaction paradigm specifically for code generation. They would be keen on exploring advanced prompt engineering techniques applicable to this domain 71, analyzing the workflow implications 6, seeing AI applied creatively 52, and critically discussing the limitations, risks, and ethical dimensions.1 There might also be interest in the potential for AI to analyze subjective qualities like aesthetics or user experience.84  
* **Workshop Focus:** A deeper dive into the underlying LLMs tuned for code. Advanced prompt engineering strategies and their effectiveness. Discussion of concepts like visually-grounded synthesis and repair.99 A strong emphasis on the limitations, ethical considerations (authorship, bias, etc.), and future trends in AI-driven software development. Less focus on basic coding exercises, more on conceptual analysis, workflow implications, and critical discussion.

This diverse range of potential attendees necessitates a flexible workshop structure. While some activities can cater to broad interests (e.g., foundational concepts, basic prompting), offering domain-specific challenges or discussion tracks in the later stages could be highly beneficial. A common thread across the creative roles is the potential for Vibe Coding to accelerate prototyping and experimentation, bridging the gap between idea and initial implementation. For the more technical audience, the focus shifts towards understanding the AI, the nuances of the workflow, advanced prompting, and the critical evaluation of limitations and ethics.

**Audience Profile Summary Table**

| Audience Profile | Key Interests/Goals | Key Challenges | Potential Vibe Coding Application/Interest | Suggested Workshop Focus Area |
| :---- | :---- | :---- | :---- | :---- |
| **Tech Artist** | Bridge art/code, tools/pipelines, shaders/VFX, optimization 14 | Balance aesthetics/performance, complex pipelines, automation, learning new tech 14 | Rapid tool prototyping, shader/VFX experiments, learning APIs/languages, simple automation 1 | Hands-on: Prompting for DCC scripts, shader snippets, procedural logic. Case studies in tech art. |
| **Game Developer** | Engaging gameplay, mechanics, world-building, optimization, iteration 33 | Scope/deadlines, technical hurdles, debugging, balancing features, game feel 34 | Rapid prototyping (mechanics), concept validation, exploring game feel, placeholder code, learning engines 1 | Hands-on: Prompting for gameplay loops, game feel variations, simple AI/UI logic. Discussing prototype-to-production pipeline. |
| **UI/UX Designer** | Intuitive interfaces, smooth flows, engagement, aesthetics, learnability 35 | Balance aesthetics/functionality, complex interactions, testing, consistency 33 | Rapid UI prototyping, testing interactions, generating visual states/animations, empowering non-coders 6 | Hands-on: Prompting for UI components, basic animations, layout variations. Discussing design-to-code gap for prototyping. |
| **Creative Coder** | Artistic expression, exploration, generative art, interactivity 44 | Blank page, idea-to-code translation, getting stuck, technical barriers 49 | Idea sketching, algorithmic exploration, adding interactivity, learning libraries, AI as collaborator 1 | Hands-on (p5.js/Processing): Prompting for generative patterns, animations, interaction. Exploring prompts for aesthetics. Discussing AI & creativity. |
| **AI Practitioner** | Build/train/deploy AI, prompt engineering, workflows, ethics, applications 71 | Reliability, safety, data governance, transparency, bias, ethics 55 | Understanding human-AI code gen interaction, prompt techniques, creative AI apps, workflow implications, limitations/ethics 1 | Deeper dive into models, advanced prompting, visually-grounded concepts 99, ethics, future trends. More discussion, less basic coding. |

## **IV. Workshop Content Deep Dive: Crafting the Experience**

This section outlines a potential structure and content for the 5-hour "Vibe Coding" workshop, divided into two main parts plus a conclusion, integrating the research findings and catering to the diverse audience profiles identified.

### **Part 1: Foundations & Exploration (Approx. 2.5 hours \+ Q\&A)**

**Goal:** To establish a common understanding of Vibe Coding, introduce the core concepts and workflow, demonstrate basic usage with relevant tools, highlight the key benefits and inherent risks, and illustrate its connections to creative technology fields. This part aims to provide foundational knowledge and initial hands-on experience.

**Proposed Concepts:**

1. **What is Vibe Coding? (Approx. 15 min)**  
   * Introduce the term, its origin with Andrej Karpathy in early 2025, and the context of increasingly powerful LLMs.1  
   * Explain the core idea: using natural language prompts to guide AI in generating, refining, and debugging code.1  
   * Present Karpathy's perspective: focusing on intent, speed, and potentially "forgetting the code exists".1  
   * Introduce Simon Willison's crucial distinction: Vibe Coding often implies *minimal review*, whereas responsible AI-assisted development demands thorough review, testing, and understanding.1 This sets the stage for critical engagement.  
2. **The Vibe Coding Workflow (Approx. 20 min)**  
   * Detail the iterative loop: Prompt \-\> Generate \-\> Test/Run \-\> Feedback \-\> Revise.3 Use a simple visual diagram.  
   * Explain the central role of natural language prompting (text or voice).1  
   * Introduce the concept of Prompt Engineering as the skill of crafting effective instructions for the AI.6 Emphasize clarity and specificity even at this basic stage.  
   * Describe the AI's role as a coding partner or assistant.3  
3. **Key Tools Showcase (Approx. 20 min)**  
   * Briefly demonstrate 2-3 popular AI coding assistants relevant to the audience (e.g., GitHub Copilot within VS Code, Cursor AI editor, potentially ChatGPT/Claude for code snippets).2  
   * Highlight key features: inline code generation (e.g., Cmd+K in Cursor 9), chat interfaces for explanation or generation 9, code completion suggestions (Tab completion 9), viewing code changes (diffs 9), context awareness (using codebase context 9), documentation integration (@Docs 9), web search capabilities (@Web 9).  
   * Mention the possibility of voice input as used by Karpathy.1  
4. **Benefits & Risks (Approx. 15 min)**  
   * Summarize the potential benefits: increased speed and productivity 3, faster prototyping and iteration 4, lowered barrier to entry and democratization 1, reduced boilerplate coding.4  
   * Clearly outline the risks: potential for bugs and errors 1, security vulnerabilities 1, poor maintainability and technical debt 1, lack of deep understanding 1, accountability issues.1  
   * Reiterate the importance of context: Vibe Coding (with minimal review) is better suited for low-stakes projects, learning, or prototypes, not critical production systems.1  
5. **Connections to Creative Fields (Approx. 15 min)**  
   * Briefly illustrate, perhaps with simple visual examples or code snippets, how Vibe Coding could be applied in:  
     * *Tech Art:* Prototyping a simple tool script, generating a basic shader effect.  
     * *Game Development:* Sketching a player movement controller, creating a simple UI interaction.  
     * *Creative Coding:* Generating a simple p5.js generative pattern or animation.  
   * This serves as a bridge to the more in-depth exploration in Part 2\.

**Proposed Activities:**

1. **Live Demo (Simple Task) (Approx. 20 min)**  
   * The presenter (Richard) performs a live coding session using a chosen AI tool (e.g., Cursor AI).  
   * Task: Create a simple, visual, interactive piece, e.g., a p5.js sketch where a shape follows the mouse and changes color on click, or a basic HTML/JS interactive element.  
   * Method: Use a mix of text and potentially voice prompts. Narrate the thought process ("inner monologue"), including how prompts are formulated and refined based on AI output.104 Intentionally encounter and fix a minor bug or unexpected AI behavior, demonstrating the iterative loop and debugging process.104 Go slowly, ensuring visibility and clarity.105  
2. **Hands-on Exercise 1 (Prompt Storming) (Approx. 15 min)**  
   * Participants individually or in pairs brainstorm and write specific prompts for simple tasks relevant to creative/technical domains.  
   * Examples: "Generate p5.js code to draw a 10x10 grid of circles with random grayscale fills." "Write a Python function for Maya that duplicates the selected object 5 times along the X-axis." "Create an HTML button that changes its text to 'Clicked\!' when pressed."  
   * Activity Focus: Encourage participants to think about clarity, specificity, and providing context in their prompts.8 Briefly discuss a few examples as a group.  
3. **Hands-on Exercise 2 (Guided Vibe Coding) (Approx. 30 min)**  
   * Participants use a designated tool/environment (pre-communicated in requirements, e.g., Cursor free tier, Replit with AI features, or VS Code \+ Copilot if available) to implement one of the prompts (either from the storming session or a provided example).  
   * Activity Focus: Experience the core prompt \-\> generate \-\> test \-\> feedback loop. Encourage trying variations or asking the AI to fix simple issues. Provide minimal starter code or setup instructions if necessary to reduce friction. The goal is successful execution of a simple task using the Vibe Coding workflow.3  
4. **Q\&A (Approx. 15 min+)**  
   * Address questions arising from the concepts and initial activities. Clarify tool usage, workflow steps, or conceptual points.

This first part ensures all participants share a foundational understanding and have had a basic, guided experience with the Vibe Coding process and tools, preparing them for more complex applications and discussions in the second half.

### **Part 2: Advanced Applications & Creative Integration (Approx. 2.5 hours \+ Q\&A)**

**Goal:** To explore more sophisticated applications of Vibe Coding within specific creative domains, delve into effective prompt engineering strategies, discuss practical integration into professional workflows, address critical ethical considerations, and consider future directions. This part emphasizes critical thinking and applying Vibe Coding to more realistic challenges.

**Proposed Concepts:**

1. **Domain-Specific Vibe Coding (Approx. 25 min)**  
   * Present more complex examples and potential use cases within:  
     * *Tech Art:* Generating more complex tool scripts, creating shader graphs or advanced shader functions (e.g., toon shading, dissolve effects 17), procedural asset generation logic (e.g., using Houdini APIs or geometry scripting 19). Show examples if possible.26  
     * *Game Development:* Prototyping more intricate interactions (e.g., simple inventory systems, state machines for AI), tuning parameters for nuanced game feel (responsiveness, viscerality 39), generating level layout ideas or logic.  
     * *Creative Coding:* Building more complex generative systems (e.g., particle systems, flocking behaviors 60), integrating external data or APIs, creating interactive installations using sensor data (conceptual link).  
   * Emphasize how Vibe Coding can accelerate exploration in these areas but stress the increased need for review and integration with traditional skills.  
2. **Prompt Engineering Techniques (Approx. 30 min)**  
   * Move beyond basic prompts to more advanced strategies for guiding the AI:  
     * *Providing Context:* Using existing code, explaining the desired architecture, leveraging codebase-aware features in tools like Cursor.9  
     * *Few-Shot Prompting:* Giving the AI 1-2 examples of the desired input/output format within the prompt to guide its generation.97  
     * *Assigning Roles/Personas:* Instructing the AI to act as an expert in a specific domain or follow certain coding standards (e.g., "Act as an expert p5.js developer...").71  
     * *Specifying Constraints:* Clearly defining output format, length, libraries to use/avoid, performance considerations.71  
     * *Iterative Refinement:* Demonstrating how to break down complex requests and refine the AI's output through follow-up prompts.8  
     * *Using Documentation/External Knowledge:* Leveraging features like Cursor's @Docs or @Web to provide the AI with specific library information or relevant online resources.9  
     * *Structuring Prompts:* Discussing best practices for organizing prompts for clarity and effectiveness.8  
3. **Integrating into Workflows (Approx. 25 min)**  
   * Discuss practical strategies for incorporating Vibe Coding into professional environments:  
     * *Hybrid Development:* Using Vibe Coding for initial drafts, prototypes, or specific modules, then transitioning to traditional coding, review, and testing for production.4  
     * *Targeted AI Assistance:* Leveraging AI for specific tasks within the development cycle, such as generating unit tests 8, writing documentation comments 8, refactoring code sections, explaining unfamiliar code, or debugging.1  
     * *Version Control:* Emphasize the importance of using version control (like Git) to manage AI-generated code, track changes, and revert if necessary.8  
     * *Managing Technical Debt:* Discuss the risks of accumulating poorly understood or suboptimal code and strategies for mitigating it (e.g., scheduled refactoring, strict code reviews for AI-generated parts).1  
4. **Ethical Considerations & Future Trends (Approx. 20 min)**  
   * Facilitate a discussion on the critical ethical and societal implications:  
     * *Authorship & Copyright:* Who owns AI-generated code? How does it impact licensing and intellectual property?.5  
     * *Originality & Creativity:* Does AI generate truly novel work, or just remix existing patterns? Impact on artistic value.54  
     * *Bias:* Potential for AI models to perpetuate biases present in their training data.  
     * *Job Displacement:* Concerns about AI automating tasks currently performed by human developers and artists.13 Discuss the likely shift in required skills rather than outright replacement.6  
     * *Responsible Use:* Emphasize the need for critical evaluation and avoiding blind trust in AI output.8  
   * Briefly touch on potential future developments: more sophisticated code generation, AI agents capable of more complex tasks 108, AI contributing to or analyzing game aesthetics/UX.84

**Proposed Activities:**

1. **Live Demo (Complex Task) (Approx. 25 min)**  
   * Presenter tackles a more challenging task relevant to the audience profiles.  
   * Examples: Generating a GLSL shader stub for a specific effect (e.g., procedural noise, simple toon shading) and integrating it into a basic scene; prototyping a game system like a simple state machine for an NPC; creating a generative art piece with multiple interacting elements and user input.  
   * Method: Focus on demonstrating advanced prompt engineering techniques discussed earlier. Show the process of breaking down the problem, iterating with the AI, debugging more complex errors, and potentially integrating generated code with manually written code.104  
2. **Hands-on Exercise 3 (Domain-Specific Challenge) (Approx. 40 min)**  
   * Participants work individually, in pairs, or small groups on a challenge tailored to their interests or assigned based on background.  
   * Challenge Examples: "Use Vibe Coding to prototype a simple UI inventory grid system with drag-and-drop placeholders." "Generate a p5.js sketch simulating basic flocking behavior (boids) responding to mouse interaction." "Attempt to generate a simple toon shader using AI assistance and apply it to a basic 3D model in a provided environment (e.g., web playground, simple Unity/Unreal scene)." "Write a Python script using AI help to automate renaming files in a specific folder structure based on predefined rules."  
   * Activity Focus: Apply concepts from Part 2, particularly advanced prompting and iterative refinement. Encourage experimentation and tackling a slightly more open-ended problem.  
3. **Group Discussion/Critique (Approx. 20 min)**  
   * Participants briefly share their results, challenges, or key learnings from the hands-on exercise.  
   * Facilitate a group discussion: What prompting strategies were effective? Where did the AI struggle? What were the limitations? How would this integrate into a real project? Encourage constructive peer feedback.  
4. **Q\&A (Approx. 15 min+)**  
   * Address more nuanced questions about specific applications, workflow integration, ethical dilemmas, advanced techniques, or future possibilities.

This second part builds upon the foundation, pushing participants to apply Vibe Coding to more realistic scenarios, think critically about its integration and limitations, and engage with the broader context of AI in creative technology.

### **Q\&A and Conclusion (Approx. 30 min \+ Q\&A)**

**Goal:** To consolidate learning, address final questions, reinforce responsible practices, provide pathways for continued exploration, and offer a concluding perspective on Vibe Coding's role.

**Proposed Content:**

1. **Final Q\&A (Approx. 10 min)**  
   * Open the floor for any remaining questions from the entire workshop.  
2. **Summary of Key Takeaways (Approx. 10 min)**  
   * Briefly recap the core concepts:  
     * Vibe Coding definition (Karpathy's intent vs. Willison's caution).1  
     * The iterative prompt-generate-test-feedback workflow.3  
     * Benefits (speed, accessibility) and Risks (quality, security, understanding).4  
     * The critical importance of human review, testing, and understanding.7  
     * The power of effective prompt engineering.8  
     * Context-specific application (prototyping, learning vs. production).  
3. **Best Practices for "Vibing" Responsibly (Approx. 5 min)**  
   * Offer concise, actionable guidelines:  
     * *Start Small & Iterate:* Break down complex problems.8  
     * *Test Early, Test Often:* Don't wait for the end to run the code.8  
     * *Review & Understand:* Especially for critical code; apply Willison's "explainability" rule.7  
     * *Use Appropriately:* Match the technique to the context (prototype vs. production).4  
     * *Prompt Clearly:* Specificity and context yield better results.71  
     * *Use Version Control:* Save working checkpoints.8  
     * *Stay Engaged:* Don't blindly trust the AI; guide and curate.8  
     * *Keep Learning:* Experiment to build intuition.7  
4. **Next Steps/Resources (Approx. 5 min)**  
   * Suggest avenues for continued learning:  
     * *Tools:* Reiterate key AI assistants and creative platforms explored (Cursor, Copilot, p5.js, etc.).11  
     * *Communities:* Point to online communities for creative coding (e.g., Processing/p5.js forums, specific subreddits, Discord servers) or generative art.50  
     * *Reading:* Recommend relevant blogs (e.g., Simon Willison's blog 7), articles on prompt engineering 71, or books on creative coding/AI.  
     * *Practice:* Encourage participants to apply Vibe Coding to small personal projects or experiments to solidify learning.7

This concluding section aims to leave participants with a clear summary, practical advice for responsible application, and resources to continue their journey with AI-assisted coding.

## **V. Refining the Workshop Narrative**

Based on the detailed content plan, the following drafts can be used to refine the workshop's descriptive elements (Abstract, Target Audience, Requirements) to accurately reflect the proposed experience.

**Draft Abstract Suggestions:**

* Option 1 (Focus on Speed/Accessibility):  
  Explore "Vibe Coding," the AI-driven paradigm transforming code creation. Coined by Andrej Karpathy, this approach uses natural language prompts to rapidly generate software.1 This 5-hour workshop dives into the Vibe Coding workflow, key AI tools (like Copilot, Cursor) 9, and prompt engineering techniques.71 We'll explore applications in tech art, game prototyping, and creative coding through hands-on exercises and live demos. Learn how to leverage AI for faster iteration and experimentation 4, while critically examining the trade-offs between speed, code quality, and maintainability.1 Discover how to "vibe" responsibly and integrate AI assistance into your creative and technical projects.  
* Option 2 (Focus on Creative Integration):  
  Bridge the gap between creative intent and technical execution with "Vibe Coding." This workshop, led by Tech Art/AI consultant Richard Rispoli, investigates how AI code generation can accelerate workflows in game development, tech art, and creative coding.18 We'll dissect the Vibe Coding phenomenon 1, contrasting rapid AI generation with responsible development practices.7 Through practical exercises using tools like p5.js 60 and AI assistants 9, you'll learn prompt engineering strategies 71 to prototype ideas, explore "game feel" 39, generate visual elements, and build simple tools. We'll discuss integrating these techniques into professional pipelines 4 and address the crucial ethical considerations.54 Leave equipped to use AI as a powerful collaborator in your creative process.

**Draft Target Audience Suggestions:**

* Broad:  
  This workshop is designed for creative and technical professionals interested in the intersection of AI and code creation. Ideal attendees include Tech Artists, Game Developers (Programmers & Designers), UI/UX Designers, Creative Coders, and AI Practitioners seeking to understand and apply AI-driven coding techniques. Participants should have some familiarity with basic programming concepts (variables, loops, functions), but deep expertise in a specific language is not required. Curiosity about AI code generation and a willingness to experiment are key.  
* More Focused (e.g., on Creative Tech):  
  Aimed at Tech Artists, Game Developers, Creative Coders, and technically-minded Designers looking to leverage AI for faster prototyping and creative exploration. If you bridge art and code 14, want to quickly test game mechanics or visual ideas 4, or seek new ways to express creativity through code 44, this workshop is for you. Basic familiarity with a scripting language (e.g., Python, JavaScript) or visual programming environment is beneficial. We will explore how Vibe Coding can augment, not replace, your existing skills.

**Draft Requirements Suggestions:**

* **Participant Requirements:**  
  * Laptop with a modern web browser (Chrome/Firefox recommended).  
  * Stable internet connection for accessing online tools/resources.  
  * (Recommended) VS Code with RooGitHub Copilot or Cursor AI extension 9). Alternatively, willingness to use a web-based IDE like Replit with AI features during the workshop. Account setup for specific AI tools might be needed (guidance provided pre-workshop).  
  * Basic understanding of programming concepts (variables, loops, functions). Familiarity with JavaScript (especially for p5.js examples 60) or Python (for scripting examples) is helpful but not mandatory.  
  * An open mind and eagerness to engage with AI tools\!  
* **Presenter/Venue Requirements:**  
  * Reliable, high-speed internet connection.  
  * Projector/Screen suitable for code display (ensure good contrast, large font size, readability from the back).105  
  * Microphone/PA system for presenter.105  
  * Whiteboard or flip chart for diagrams/notes.104  
  * Power outlets accessible to participants.  
  * (Optional but helpful) Pre-workshop communication channel (e.g., Slack/Discord) for sharing setup instructions, links, and handling pre-workshop Q\&A.  
  * Access/accounts for specific AI tools the presenter plans to demo or use in exercises (e.g., ensure necessary subscriptions like Cursor Pro are active if required features are planned).

These refined descriptions aim to accurately represent the workshop's content, manage attendee expectations, and ensure a smooth technical experience. The Abstract should be engaging while reflecting the core tension of Vibe Coding (speed vs. responsibility). The Target Audience description helps attendees self-select based on their background and goals. The Requirements list provides practical necessities for participation and delivery, minimizing potential friction during the hands-on segments.

## **VI. Conclusion & Next Steps**

This report provides a comprehensive content strategy for a 5-hour workshop on Vibe Coding, tailored for Richard Rispoli's expertise and aimed at a diverse audience of creative and technical professionals.

**Summary of Recommendations:**

The proposed workshop structure is built upon several key pillars:

1. **Clear Definition:** Establishing a nuanced understanding of Vibe Coding, including its origins, core workflow, and the critical distinction between rapid AI generation and responsible, reviewed AI-assisted development.  
2. **Creative Connections:** Explicitly linking Vibe Coding concepts to practical applications within Tech Art, Game Development, Creative Coding, and the pursuit of specific Aesthetics and "Feel."  
3. **Audience Tailoring:** Recognizing the diverse backgrounds of potential attendees and suggesting ways to customize content and activities (especially in Part 2\) to maximize relevance and engagement for different profiles.  
4. **Hands-on Experience:** Integrating practical exercises and live demonstrations throughout the workshop, progressing from simple, guided tasks to more complex, domain-specific challenges.  
5. **Critical Perspective:** Incorporating discussions on workflow integration, the limitations of AI, technical debt, and crucial ethical considerations like authorship and bias.

The narrative arc progresses from foundational understanding and tool familiarization to advanced application, practical integration, and critical reflection, culminating in actionable best practices and resources for continued learning.

**Next Steps for Richard Rispoli:**

1. **Review and Feedback:** Thoroughly review this detailed content outline and analysis. Provide feedback on the proposed structure, concepts, activities, and examples to ensure alignment with personal expertise and vision for the workshop.  
2. **Tool Selection:** Finalize the specific AI coding assistants (e.g., Cursor, Copilot, web-based tools) and creative environments (e.g., p5.js web editor, local Processing, simple engine setup) to be used for demos and hands-on exercises. Ensure accessibility for participants based on the requirements.  
3. **Example Curation:** Select or prepare specific, compelling code examples and case studies to illustrate concepts in both Part 1 and Part 2\. These should be relevant to the target audience profiles.  
4. **Exercise Refinement:** Detail the specific tasks for the hands-on exercises (Guided Vibe Coding, Domain-Specific Challenge), ensuring they are achievable within the allotted time and provide meaningful learning experiences. Prepare any necessary starter code or project templates.  
5. **Material Preparation:** Develop the presentation slides, incorporating key definitions, diagrams (e.g., workflow loop), code snippets, and discussion prompts based on this report. Prepare any code repositories or online resources needed for the exercises.  
6. **Logistics Check:** Confirm venue requirements and ensure participant requirements (including potential pre-workshop setup for AI tools) are clearly communicated well in advance of the June 12th submission date and the workshop itself.

By leveraging this detailed content strategy, the "Vibe Coding" workshop can be positioned as an insightful, practical, and engaging experience that equips attendees with both the skills to utilize AI code generation effectively and the critical awareness to do so responsibly within their respective creative and technical domains.

#### **Sources des citations**

1. Vibe coding \- Wikipedia, consulté le mai 1, 2025, [https://en.wikipedia.org/wiki/Vibe\_coding](https://en.wikipedia.org/wiki/Vibe_coding)  
2. What is the exact definition of "vibe coding"? : r/ClaudeAI \- Reddit, consulté le mai 1, 2025, [https://www.reddit.com/r/ClaudeAI/comments/1j6z4ft/what\_is\_the\_exact\_definition\_of\_vibe\_coding/](https://www.reddit.com/r/ClaudeAI/comments/1j6z4ft/what_is_the_exact_definition_of_vibe_coding/)  
3. What is Vibe Coding? AI-powered Software Development Explained \- ZBrain, consulté le mai 1, 2025, [https://zbrain.ai/what-is-vibe-coding/](https://zbrain.ai/what-is-vibe-coding/)  
4. Is Vibe Coding Agile or Merely a Hype? \- Age-of-Product.com, consulté le mai 1, 2025, [https://age-of-product.com/vibe-coding-agile/](https://age-of-product.com/vibe-coding-agile/)  
5. The Rise of Vibe Coding and Why IP Protection Matters More Than Ever, consulté le mai 1, 2025, [https://arapackelaw.com/patents/vibe-coding-ip-protection/](https://arapackelaw.com/patents/vibe-coding-ip-protection/)  
6. Vibe Coding: The Future of AI-Driven Software Development \- Ajith's AI Pulse, consulté le mai 1, 2025, [https://ajithp.com/2025/04/14/vibe-coding-ai-software-development/](https://ajithp.com/2025/04/14/vibe-coding-ai-software-development/)  
7. Not all AI-assisted programming is vibe coding (but vibe coding rocks), consulté le mai 1, 2025, [https://simonwillison.net/2025/Mar/19/vibe-coding/](https://simonwillison.net/2025/Mar/19/vibe-coding/)  
8. r/vibecoders \- Reddit, consulté le mai 1, 2025, [https://www.reddit.com/r/vibecoders/](https://www.reddit.com/r/vibecoders/)  
9. Cursor AI: A Guide With 10 Practical Examples \- DataCamp, consulté le mai 1, 2025, [https://www.datacamp.com/tutorial/cursor-ai-code-editor](https://www.datacamp.com/tutorial/cursor-ai-code-editor)  
10. Vibe Coding Hacks: Top 10 Tips You'll Wish You Knew Sooner, consulté le mai 1, 2025, [https://www.nucamp.co/blog/vibe-coding-vibe-coding-hacks-top-10-tips-youll-wish-you-knew-sooner](https://www.nucamp.co/blog/vibe-coding-vibe-coding-hacks-top-10-tips-youll-wish-you-knew-sooner)  
11. Top 15 AI-Assisted Coding and Code Generation Tools to Try in 2025 \- DEV Community, consulté le mai 1, 2025, [https://dev.to/angelocodes/top-15-ai-assisted-coding-and-code-generation-tools-to-try-in-2025-o4g](https://dev.to/angelocodes/top-15-ai-assisted-coding-and-code-generation-tools-to-try-in-2025-o4g)  
12. The Future of Vibe Coding: How AI-Driven Development Could Transform Programming by 2030, consulté le mai 1, 2025, [https://www.nucamp.co/blog/vibe-coding-the-future-of-vibe-coding-how-aidriven-development-could-transform-programming-by-2030](https://www.nucamp.co/blog/vibe-coding-the-future-of-vibe-coding-how-aidriven-development-could-transform-programming-by-2030)  
13. (PDF) Designing Participatory AI: Creative Professionals' Worries and Expectations about Generative AI \- ResearchGate, consulté le mai 1, 2025, [https://www.researchgate.net/publication/370177840\_Designing\_Participatory\_AI\_Creative\_Professionals'\_Worries\_and\_Expectations\_about\_Generative\_AI](https://www.researchgate.net/publication/370177840_Designing_Participatory_AI_Creative_Professionals'_Worries_and_Expectations_about_Generative_AI)  
14. Mastering Video Game Character Design \- Innovecs, consulté le mai 1, 2025, [https://innovecs.com/blog/the-role-of-technical-art-in-video-game-character-design/](https://innovecs.com/blog/the-role-of-technical-art-in-video-game-character-design/)  
15. Who Is a Technical Artist? Responsibilities & Required Skill \- Pixune Studios, consulté le mai 1, 2025, [https://pixune.com/blog/who-is-a-technical-artist/](https://pixune.com/blog/who-is-a-technical-artist/)  
16. Technical Artist \- Everything You Need To Know \- NFI, consulté le mai 1, 2025, [https://www.nfi.edu/technical-artist/3/](https://www.nfi.edu/technical-artist/3/)  
17. Technical Artist Course | Online Education for Game Development | ELVTR, consulté le mai 1, 2025, [https://elvtr.com/course/technical-art](https://elvtr.com/course/technical-art)  
18. What's your thought on the future of AI use in the game industry? : r/gamedev \- Reddit, consulté le mai 1, 2025, [https://www.reddit.com/r/gamedev/comments/1hwo5q9/whats\_your\_thought\_on\_the\_future\_of\_ai\_use\_in\_the/](https://www.reddit.com/r/gamedev/comments/1hwo5q9/whats_your_thought_on_the_future_of_ai_use_in_the/)  
19. FIT3097 \- Technical art \- Monash University Handbook, consulté le mai 1, 2025, [https://handbook.monash.edu/2025/units/FIT3097](https://handbook.monash.edu/2025/units/FIT3097)  
20. Creative Chronicles: VFX, consulté le mai 1, 2025, [https://www.creative-assembly.com/blog/creative-chronicles-vfx](https://www.creative-assembly.com/blog/creative-chronicles-vfx)  
21. What Is a Toon Shader? | Toon-Shading Software \- Autodesk, consulté le mai 1, 2025, [https://www.autodesk.com/solutions/toon-shader](https://www.autodesk.com/solutions/toon-shader)  
22. Cel Shading Technique: Guide, Definition, and Tools | RebusFarm, consulté le mai 1, 2025, [https://rebusfarm.net/blog/how-to-do-cel-shading-techniques-tools](https://rebusfarm.net/blog/how-to-do-cel-shading-techniques-tools)  
23. An introduction to Shader Art Coding \- YouTube, consulté le mai 1, 2025, [https://www.youtube.com/watch?v=f4s1h2YETNY](https://www.youtube.com/watch?v=f4s1h2YETNY)  
24. Stylized toon shaders in Godot part 1 \- Baldur Games, consulté le mai 1, 2025, [https://baldurgames.com/posts/stylized-shaders-godot](https://baldurgames.com/posts/stylized-shaders-godot)  
25. 3 Simple Stylized Toon Shaders for Creating 2D/3D Artworks in Blender \- YouTube, consulté le mai 1, 2025, [https://www.youtube.com/watch?v=vRALvQSS1vw\&pp=0gcJCdgAo7VqN5tD](https://www.youtube.com/watch?v=vRALvQSS1vw&pp=0gcJCdgAo7VqN5tD)  
26. Tech Art Aid videos \- shaders, procedural generation, etc \- Unreal Engine Forums, consulté le mai 1, 2025, [https://forums.unrealengine.com/t/tech-art-aid-videos-shaders-procedural-generation-etc/69268](https://forums.unrealengine.com/t/tech-art-aid-videos-shaders-procedural-generation-etc/69268)  
27. Transitioning into Tech Art from Game Programming : r/TechnicalArtist \- Reddit, consulté le mai 1, 2025, [https://www.reddit.com/r/TechnicalArtist/comments/1b969hh/transitioning\_into\_tech\_art\_from\_game\_programming/](https://www.reddit.com/r/TechnicalArtist/comments/1b969hh/transitioning_into_tech_art_from_game_programming/)  
28. Anouk Donkers tech art portfolio 2022, by AnoukDonkers \- The Rookies, consulté le mai 1, 2025, [https://www.therookies.co/entries/17418](https://www.therookies.co/entries/17418)  
29. From Ubisoft Toronto's NEXT to Working as a Tech Artist \- 80 Level, consulté le mai 1, 2025, [https://80.lv/articles/from-ubisoft-toronto-s-next-challenge-to-working-as-a-tech-artist/](https://80.lv/articles/from-ubisoft-toronto-s-next-challenge-to-working-as-a-tech-artist/)  
30. Visualizing Equations Vol. 2 \- Shaders and Procedural Shapes for Technical Art \- Jettelly, consulté le mai 1, 2025, [https://jettelly.com/store/visualizing-equations-vol-2](https://jettelly.com/store/visualizing-equations-vol-2)  
31. Tech Artist Portfolio: John O'Really, consulté le mai 1, 2025, [https://johno.re/](https://johno.re/)  
32. What are some cool examples of procedural pixel shader effects? \[closed\], consulté le mai 1, 2025, [https://gamedev.stackexchange.com/questions/2419/what-are-some-cool-examples-of-procedural-pixel-shader-effects](https://gamedev.stackexchange.com/questions/2419/what-are-some-cool-examples-of-procedural-pixel-shader-effects)  
33. Exploring Game Design Challenges: Overcoming obstacles in the development process, consulté le mai 1, 2025, [https://moldstud.com/articles/p-exploring-game-design-challenges-overcoming-obstacles-in-the-development-process](https://moldstud.com/articles/p-exploring-game-design-challenges-overcoming-obstacles-in-the-development-process)  
34. Game Development Challenges \- Juego Studios, consulté le mai 1, 2025, [https://www.juegostudio.com/blog/top-8-common-problems-faced-by-game-developers-and-how-to-fix-them](https://www.juegostudio.com/blog/top-8-common-problems-faced-by-game-developers-and-how-to-fix-them)  
35. Game UX — Blending Game Design and User Experience \- UXPin, consulté le mai 1, 2025, [https://www.uxpin.com/studio/blog/game-ux/](https://www.uxpin.com/studio/blog/game-ux/)  
36. Your Guide to Top-notch And Powerful Mobile Game Design \- Expert App Devs, consulté le mai 1, 2025, [https://www.expertappdevs.com/blog/mobile-game-design](https://www.expertappdevs.com/blog/mobile-game-design)  
37. Dynamic 3D Modeling in Game Design Aesthetics \- Agicent, consulté le mai 1, 2025, [https://www.agicent.com/blog/dynamic-3d-modeling-in-game-design-aesthetics/](https://www.agicent.com/blog/dynamic-3d-modeling-in-game-design-aesthetics/)  
38. What We Talk About When We Talk About Game Aesthetics \- DiVA portal, consulté le mai 1, 2025, [http://www.diva-portal.org/smash/get/diva2:1408066/FULLTEXT01.pdf](http://www.diva-portal.org/smash/get/diva2:1408066/FULLTEXT01.pdf)  
39. Game Feel: A Beginner's Guide \- Game Design Skills, consulté le mai 1, 2025, [https://gamedesignskills.com/game-design/game-feel/](https://gamedesignskills.com/game-design/game-feel/)  
40. Developer of Celeste shares some cool game-feel tips\! : r/gamedev \- Reddit, consulté le mai 1, 2025, [https://www.reddit.com/r/gamedev/comments/fhzw5f/developer\_of\_celeste\_shares\_some\_cool\_gamefeel/](https://www.reddit.com/r/gamedev/comments/fhzw5f/developer_of_celeste_shares_some_cool_gamefeel/)  
41. Squeezing more juice out of your game design\! \- GameAnalytics, consulté le mai 1, 2025, [https://gameanalytics.com/blog/squeezing-more-juice-out-of-your-game-design/](https://gameanalytics.com/blog/squeezing-more-juice-out-of-your-game-design/)  
42. What are your go-to ways to making your game feel better quick? : r/gamedev \- Reddit, consulté le mai 1, 2025, [https://www.reddit.com/r/gamedev/comments/te07sm/what\_are\_your\_goto\_ways\_to\_making\_your\_game\_feel/](https://www.reddit.com/r/gamedev/comments/te07sm/what_are_your_goto_ways_to_making_your_game_feel/)  
43. How To Make Your Game Feel Better \- YouTube, consulté le mai 1, 2025, [https://www.youtube.com/watch?v=TfxGfhr7Bhw](https://www.youtube.com/watch?v=TfxGfhr7Bhw)  
44. Aesthetic Coding: Exploring Computational Culture Beyond Creative ..., consulté le mai 1, 2025, [https://pure.au.dk/portal/en/publications/aesthetic-coding-exploring-computational-culture-beyond-creative-coding(e3a8a068-1ae3-44bc-b64c-73cfd77d1586).html](https://pure.au.dk/portal/en/publications/aesthetic-coding-exploring-computational-culture-beyond-creative-coding\(e3a8a068-1ae3-44bc-b64c-73cfd77d1586\).html)  
45. Artistic Sketching for Expressive Coding \- Eurographics Association, consulté le mai 1, 2025, [https://diglib.eg.org/items/ba0ab144-ed5e-4f9e-925c-8835b920acf4](https://diglib.eg.org/items/ba0ab144-ed5e-4f9e-925c-8835b920acf4)  
46. Debugging for Art's Sake: Beginning Programmers' Debugging ..., consulté le mai 1, 2025, [https://repository.isls.org/handle/1/6319](https://repository.isls.org/handle/1/6319)  
47. Creative Coding and Generative Art: Tips and Tricks \- Yellowbrick, consulté le mai 1, 2025, [https://www.yellowbrick.co/blog/animation/creative-coding-and-generative-art-tips-and-tricks](https://www.yellowbrick.co/blog/animation/creative-coding-and-generative-art-tips-and-tricks)  
48. Creative Coding: The New Era \- Gorilla Sun, consulté le mai 1, 2025, [https://www.gorillasun.de/blog/creative-coding-the-new-era/](https://www.gorillasun.de/blog/creative-coding-the-new-era/)  
49. TEACHING AND LEARNING CREATIVE CODING WITH CONVERSATIONAL AI \- GLOKALde, consulté le mai 1, 2025, [https://www.glokalde.com/pdf/issues/26/Article3.pdf](https://www.glokalde.com/pdf/issues/26/Article3.pdf)  
50. Getting Started with Processing Creative Coding: A Complete Guide | Steve Zafeiriou, consulté le mai 1, 2025, [https://stevezafeiriou.com/processing-creative-coding/](https://stevezafeiriou.com/processing-creative-coding/)  
51. terkelg/awesome-creative-coding: Creative Coding: Generative Art, Data visualization, Interaction Design, Resources. \- GitHub, consulté le mai 1, 2025, [https://github.com/terkelg/awesome-creative-coding](https://github.com/terkelg/awesome-creative-coding)  
52. Creative Coding Empowering AI Artists Through Programming \- AI Art Kingdom, consulté le mai 1, 2025, [https://www.aiartkingdom.com/post/creative-coding-ai](https://www.aiartkingdom.com/post/creative-coding-ai)  
53. Exploring User Engagement and Interaction in Generating Abstract Imagery \- kth .diva, consulté le mai 1, 2025, [https://kth.diva-portal.org/smash/get/diva2:1942260/FULLTEXT02.pdf](https://kth.diva-portal.org/smash/get/diva2:1942260/FULLTEXT02.pdf)  
54. 2021-09: Creative Coding: Generative / Algorithmic Art and the Exploration of Authorship and Authenticity – ACM SIGGRAPH DAC, consulté le mai 1, 2025, [https://dac.siggraph.org/sparks/2021-09-creative-coding-generative-algorithmic-art-and-the-exploration-of-authorship-and-authenticity/](https://dac.siggraph.org/sparks/2021-09-creative-coding-generative-algorithmic-art-and-the-exploration-of-authorship-and-authenticity/)  
55. (PDF) The Paradox of Artificial Creativity: Challenges and Opportunities of Generative AI Artistry \- ResearchGate, consulté le mai 1, 2025, [https://www.researchgate.net/publication/381037114\_The\_Paradox\_of\_Artificial\_Creativity\_Challenges\_and\_Opportunities\_of\_Generative\_AI\_Artistry](https://www.researchgate.net/publication/381037114_The_Paradox_of_Artificial_Creativity_Challenges_and_Opportunities_of_Generative_AI_Artistry)  
56. Comparing Top Generative Art Tools: Processing, OpenFrameworks, P5.js, and More, consulté le mai 1, 2025, [https://visualalchemist.in/2024/08/31/comparing-top-generative-art-tools-processing-openframeworks-p5-js-and-more/](https://visualalchemist.in/2024/08/31/comparing-top-generative-art-tools-processing-openframeworks-p5-js-and-more/)  
57. Tezos Ecosystem Explores Generative Art in Creative Coding Workshop \- Blockchain.News, consulté le mai 1, 2025, [https://blockchain.news/news/tezos-ecosystem-explores-generative-art-in-creative-coding-workshop](https://blockchain.news/news/tezos-ecosystem-explores-generative-art-in-creative-coding-workshop)  
58. Generative Collage: Exploring your Creative Practice with Code (P0408-24), consulté le mai 1, 2025, [https://www.andersonranch.org/workshops/workshop/generative-collage-exploring-your-creative-practice-with-code-p0408-24/](https://www.andersonranch.org/workshops/workshop/generative-collage-exploring-your-creative-practice-with-code-p0408-24/)  
59. Planned Activities | Collaborative Creative Coding Through Drawing Robots, consulté le mai 1, 2025, [https://liciahe.github.io/plotter\_party\_2022/Schedule.html](https://liciahe.github.io/plotter_party_2022/Schedule.html)  
60. Examples \- p5.js, consulté le mai 1, 2025, [https://p5js.org/examples/](https://p5js.org/examples/)  
61. p5.js Coding Tutorial | Procedural Terrain Generation (Perlin Noise) \- YouTube, consulté le mai 1, 2025, [https://www.youtube.com/watch?v=fN0Wa9mvT60](https://www.youtube.com/watch?v=fN0Wa9mvT60)  
62. How to Code Procedural Terrain with Perlin Noise (JavaScript & p5.js) \- YouTube, consulté le mai 1, 2025, [https://www.youtube.com/watch?v=ZoqPQ0sFo6A](https://www.youtube.com/watch?v=ZoqPQ0sFo6A)  
63. Getting Started with p5.js \- City Tech OpenLab, consulté le mai 1, 2025, [https://openlab.citytech.cuny.edu/mtec1101-hd88-sp2022/files/2019/03/Make\_Getting-Started-with-p5dotjs.pdf](https://openlab.citytech.cuny.edu/mtec1101-hd88-sp2022/files/2019/03/Make_Getting-Started-with-p5dotjs.pdf)  
64. I created a library for p5.js to create color palettes easily and now I'm sharing it with everyone else. https://github.com/alexandru-postolache/p5.colorGenerator : r/creativecoding \- Reddit, consulté le mai 1, 2025, [https://www.reddit.com/r/creativecoding/comments/1fft7u4/i\_created\_a\_library\_for\_p5js\_to\_create\_color/](https://www.reddit.com/r/creativecoding/comments/1fft7u4/i_created_a_library_for_p5js_to_create_color/)  
65. Part 01 | The aesthetic of generative coding \- GitHub Pages, consulté le mai 1, 2025, [https://digitalideation.github.io/ba\_222\_gencg\_h1801/notebooks/week01.html](https://digitalideation.github.io/ba_222_gencg_h1801/notebooks/week01.html)  
66. Generative Graphics Tools for Raspberry Pi \- The Interactive & Immersive HQ, consulté le mai 1, 2025, [https://interactiveimmersive.io/blog/interactive-media/generative-graphics-tools-for-raspberry-pi/](https://interactiveimmersive.io/blog/interactive-media/generative-graphics-tools-for-raspberry-pi/)  
67. 1: Getting Started with p5.js: How to Code Generative Art \- YouTube, consulté le mai 1, 2025, [https://www.youtube.com/watch?v=6QFw\_vWkFTI](https://www.youtube.com/watch?v=6QFw_vWkFTI)  
68. The 3 Creative Coding Challenges That Never Get Mentioned, consulté le mai 1, 2025, [https://www.apress.com/fr/blog/all-blog-posts/the-3-creative-coding-challenges-that-never-get-mentioned/18807722](https://www.apress.com/fr/blog/all-blog-posts/the-3-creative-coding-challenges-that-never-get-mentioned/18807722)  
69. What I made at the Recurse Center | Gianluca.ai, consulté le mai 1, 2025, [https://gianluca.ai/made-at-recurse/](https://gianluca.ai/made-at-recurse/)  
70. deciding between processing and touchdesigner : r/creativecoding \- Reddit, consulté le mai 1, 2025, [https://www.reddit.com/r/creativecoding/comments/u7o7e5/deciding\_between\_processing\_and\_touchdesigner/](https://www.reddit.com/r/creativecoding/comments/u7o7e5/deciding_between_processing_and_touchdesigner/)  
71. Prompt Engineering Best Practices: Tips, Tricks, and Tools | DigitalOcean, consulté le mai 1, 2025, [https://www.digitalocean.com/resources/articles/prompt-engineering-best-practices](https://www.digitalocean.com/resources/articles/prompt-engineering-best-practices)  
72. The Role of Artwork in Game Design: Aesthetic vs. Functionality, consulté le mai 1, 2025, [https://mahtgiciangames.com/blogs/the-creative-workshop-game-design-blueprints/the-role-of-artwork-in-game-design-aesthetic-vs-functionality](https://mahtgiciangames.com/blogs/the-creative-workshop-game-design-blueprints/the-role-of-artwork-in-game-design-aesthetic-vs-functionality)  
73. 7 Incredible Game Design Examples And Why They Work \- GameAnalytics, consulté le mai 1, 2025, [https://gameanalytics.com/blog/incredible-game-design-examples/](https://gameanalytics.com/blog/incredible-game-design-examples/)  
74. Game UX Design: Why UX is Important in 3D Video Game ..., consulté le mai 1, 2025, [https://kevurugames.com/blog/game-ux-design-why-ux-is-important-in-3d-video-game-development/](https://kevurugames.com/blog/game-ux-design-why-ux-is-important-in-3d-video-game-development/)  
75. The Impact of Visual Style on User Experience in Games \- ResearchGate, consulté le mai 1, 2025, [https://www.researchgate.net/publication/322323740\_The\_Impact\_of\_Visual\_Style\_on\_User\_Experience\_in\_Games](https://www.researchgate.net/publication/322323740_The_Impact_of_Visual_Style_on_User_Experience_in_Games)  
76. The Influence of Aesthetic Factors on Game Immersion through the Player Involvement Model \- IRE Journals, consulté le mai 1, 2025, [https://www.irejournals.com/formatedpaper/1705440.pdf](https://www.irejournals.com/formatedpaper/1705440.pdf)  
77. Aesthetic Coding \- TikTok, consulté le mai 1, 2025, [https://www.tiktok.com/discover/aesthetic-coding](https://www.tiktok.com/discover/aesthetic-coding)  
78. What is Affective Computing? \- DataCamp, consulté le mai 1, 2025, [https://www.datacamp.com/blog/what-is-affective-computing](https://www.datacamp.com/blog/what-is-affective-computing)  
79. Top 25+ Affective Computing Applications: Emotion AI Use Cases \- Research AIMultiple, consulté le mai 1, 2025, [https://research.aimultiple.com/affective-computing-applications/](https://research.aimultiple.com/affective-computing-applications/)  
80. Affective Computing: Designing for Human-Computer Interaction \- Koombea, consulté le mai 1, 2025, [https://www.koombea.com/blog/affective-computing-designing-for-human-computer-interaction/](https://www.koombea.com/blog/affective-computing-designing-for-human-computer-interaction/)  
81. Unlocking Emotional Intelligence in Technology: The Rise of Affective Computing, consulté le mai 1, 2025, [https://www.morphcast.com/the-rise-of-affective-computing/](https://www.morphcast.com/the-rise-of-affective-computing/)  
82. Affective Computing: In-Depth Guide to Emotion AI in 2025 \- Research AIMultiple, consulté le mai 1, 2025, [https://research.aimultiple.com/affective-computing/](https://research.aimultiple.com/affective-computing/)  
83. Affective Computing | The Encyclopedia of Human-Computer Interaction, 2nd Ed., consulté le mai 1, 2025, [https://www.interaction-design.org/literature/book/the-encyclopedia-of-human-computer-interaction-2nd-ed/affective-computing](https://www.interaction-design.org/literature/book/the-encyclopedia-of-human-computer-interaction-2nd-ed/affective-computing)  
84. This Game SUX: Why & How to Design Sh@\*\!y User Experiences, consulté le mai 1, 2025, [https://exertiongameslab.org/wp-content/uploads/2025/04/sux\_chi2025.pdf](https://exertiongameslab.org/wp-content/uploads/2025/04/sux_chi2025.pdf)  
85. Towards Qualia-Driven Game Design \- DiGRA Digital Library, consulté le mai 1, 2025, [https://dl.digra.org/index.php/dl/article/download/2243/2240/2258](https://dl.digra.org/index.php/dl/article/download/2243/2240/2258)  
86. Artificial intelligence for video game visualization, advancements, benefits and challenges, consulté le mai 1, 2025, [https://www.aimspress.com/article/doi/10.3934/mbe.2023686?viewType=HTML](https://www.aimspress.com/article/doi/10.3934/mbe.2023686?viewType=HTML)  
87. The Future of the Swedish Gaming Industry in an AI Era: the impact on competencies and skills \- DiVA portal, consulté le mai 1, 2025, [https://su.diva-portal.org/smash/get/diva2:1955757/FULLTEXT01.pdf](https://su.diva-portal.org/smash/get/diva2:1955757/FULLTEXT01.pdf)  
88. GDC 2025 \- Our Highlights \- RapidPipeline, consulté le mai 1, 2025, [https://rapidpipeline.com/en/blog/gdc-2025](https://rapidpipeline.com/en/blog/gdc-2025)  
89. Blog \- The Toolsmiths, consulté le mai 1, 2025, [https://thetoolsmiths.org/blog](https://thetoolsmiths.org/blog)  
90. Towards Responsible AI Music: an Investigation of Trustworthy Features for Creative Systems \- arXiv, consulté le mai 1, 2025, [https://arxiv.org/html/2503.18814v1](https://arxiv.org/html/2503.18814v1)  
91. Responsible AI in the Arts: How Creative Disciplines are Shaping AI Developments Everywhere, consulté le mai 1, 2025, [https://www.responsible.ai/responsible-ai-in-the-arts-how-creative-disciplines-are-shaping-ai-developments-everywhere/](https://www.responsible.ai/responsible-ai-in-the-arts-how-creative-disciplines-are-shaping-ai-developments-everywhere/)  
92. Generative AI and Creative Work: Narratives, Values, and Impacts \- arXiv, consulté le mai 1, 2025, [https://arxiv.org/html/2502.03940](https://arxiv.org/html/2502.03940)  
93. (PDF) Generative AI and its Applications in Creative Industries \- ResearchGate, consulté le mai 1, 2025, [https://www.researchgate.net/publication/385508903\_Generative\_AI\_and\_its\_Applications\_in\_Creative\_Industries](https://www.researchgate.net/publication/385508903_Generative_AI_and_its_Applications_in_Creative_Industries)  
94. \[Keeping Tempo With Music Biz\] — Tackling the Challenges Presented by Generative AI in Music: An Interview with ARS Counsel's Almuhtada Smith, consulté le mai 1, 2025, [https://musicbiz.org/news/keeping-tempo-with-music-biz-tackling-the-challenges-presented-by-generative-ai-in-music-an-interview-with-ars-counsels-almuhtada-smith/](https://musicbiz.org/news/keeping-tempo-with-music-biz-tackling-the-challenges-presented-by-generative-ai-in-music-an-interview-with-ars-counsels-almuhtada-smith/)  
95. The Revolution of Generative AI Music: Opportunities and Challenges \- MusicHub, consulté le mai 1, 2025, [https://www.music-hub.com/en-blog/the-revolution-of-generative-ai-music-opportunities-and-challenges](https://www.music-hub.com/en-blog/the-revolution-of-generative-ai-music-opportunities-and-challenges)  
96. Engaging with AI painting: exploring motivations and challenges in laypeople's creative information practices, consulté le mai 1, 2025, [https://informationr.net/infres/article/download/856/434?inline=1](https://informationr.net/infres/article/download/856/434?inline=1)  
97. Prompt engineering: The process, uses, techniques, applications and best practices, consulté le mai 1, 2025, [https://www.leewayhertz.com/prompt-engineering/](https://www.leewayhertz.com/prompt-engineering/)  
98. AI Prompt Engineering Examples, Tactics, & Techniques \- eWEEK, consulté le mai 1, 2025, [https://www.eweek.com/artificial-intelligence/prompt-engineering-examples/](https://www.eweek.com/artificial-intelligence/prompt-engineering-examples/)  
99. LogoMotion: Visually-Grounded Code Synthesis for Creating and Editing Animation \- arXiv, consulté le mai 1, 2025, [https://arxiv.org/html/2405.07065v2](https://arxiv.org/html/2405.07065v2)  
100. Shader art, links, and assorted ponderings | Weeknotes | Gianluca.ai, consulté le mai 1, 2025, [https://gianluca.ai/2024-40/](https://gianluca.ai/2024-40/)  
101. (PDF) Artificial intelligence for video game visualization, advancements, benefits and challenges \- ResearchGate, consulté le mai 1, 2025, [https://www.researchgate.net/publication/372564528\_Artificial\_intelligence\_for\_video\_game\_visualization\_advancements\_benefits\_and\_challenges](https://www.researchgate.net/publication/372564528_Artificial_intelligence_for_video_game_visualization_advancements_benefits_and_challenges)  
102. Challenges in Generating Juice Effects for Automatically Designed Games, consulté le mai 1, 2025, [https://ojs.aaai.org/index.php/AIIDE/article/download/18889/18654/22655](https://ojs.aaai.org/index.php/AIIDE/article/download/18889/18654/22655)  
103. Best Zemith Alternatives & Competitors \- SourceForge, consulté le mai 1, 2025, [https://sourceforge.net/software/product/Zemith/alternatives](https://sourceforge.net/software/product/Zemith/alternatives)  
104. Live coding \- Raspberrypi, consulté le mai 1, 2025, [https://static.raspberrypi.org/files/curriculum/quickreads/5-Pedagogy\_Summary\_Live\_Coding\_V4.pdf](https://static.raspberrypi.org/files/curriculum/quickreads/5-Pedagogy_Summary_Live_Coding_V4.pdf)  
105. Live Coding is a Skill \- Galaxy Training\!, consulté le mai 1, 2025, [https://training.galaxyproject.org/training-material/topics/teaching/tutorials/live-coding/tutorial.html](https://training.galaxyproject.org/training-material/topics/teaching/tutorials/live-coding/tutorial.html)  
106. Ten quick tips for teaching with (participatory) live coding (online) | Yanina Bellini Saibene, consulté le mai 1, 2025, [https://yabellini.netlify.app/blog/2022\_teaching\_en/04-teaching/](https://yabellini.netlify.app/blog/2022_teaching_en/04-teaching/)  
107. Ten quick tips for teaching with participatory live coding \- PMC, consulté le mai 1, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC7482837/](https://pmc.ncbi.nlm.nih.gov/articles/PMC7482837/)  
108. moussaclarke/awesome-stars \- GitHub, consulté le mai 1, 2025, [https://github.com/moussaclarke/awesome-stars](https://github.com/moussaclarke/awesome-stars)