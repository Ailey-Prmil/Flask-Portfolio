from .section_controller import FullName, JobTitle, SkillTag, AboutMe, Contact, Config, Education, Experience, Project, Certificate, Skill

from .file_controller import File_Manager


class Portfolio:
    def __init__(self):
        self.full_name = FullName()
        self.jobtitles = JobTitle()
        self.skill_tags = SkillTag()
        self.about_me = AboutMe()
        self.contact = Contact()
        self.config = Config()
        self.skills = Skill()
        self.educations = Education()
        self.experiences = Experience()
        self.projects = Project()
        self.certificates = Certificate()        
    
    def __str__(self):
        return str({
            "full_name": self.full_name,
            "job_titles": self.jobtitles,
            "skill_tags": self.skill_tags,
            "about_me": self.about_me,
            "contact": self.contact,
            "config": self.config,
            "skills": self.skills,
            "educations": self.educations,
            "experiences": self.experiences,
            "projects": self.projects
        })
    
    def save_file(self):
        file_manager = File_Manager()
        file_manager.save_file(self)

request = {
    
}
