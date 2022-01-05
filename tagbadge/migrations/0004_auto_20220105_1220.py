# Generated by Django 3.2.6 on 2021-11-27 15:05

from django.db import migrations

from django.db import migrations
from django.utils import timezone

def saveTagBadge(apps, schema_editor):
    TagBadge = apps.get_model("tagbadge", "TagBadge")
    TagBadge.objects.get_or_create(badge_type="BRONZE",description="First bounty you manually award on another person's question", tag_name="Altruist",date=timezone.now(),preBuild=True, bade_position="Tag", url="#")
    TagBadge.objects.get_or_create(badge_type="BRONZE",description="First bounty you manually award on your own question", tag_name="Benefactor",date=timezone.now(),preBuild=True, bade_position="Tag", url="#")
    TagBadge.objects.get_or_create(badge_type="SILVER",description="Question bookmarked by 25 users", tag_name="Favorite Question",date=timezone.now(),preBuild=True, bade_position="Tag", url="#")
    TagBadge.objects.get_or_create(badge_type="GOLD",description="Question bookmarked by 100 users", tag_name="Stellar Question",date=timezone.now(),preBuild=True, bade_position="Tag", url="#")
    TagBadge.objects.get_or_create(badge_type="BRONZE",description="First bounty you offer on another person's question", tag_name="Investor",date=timezone.now(),preBuild=True, bade_position="Tag", url="#")
    TagBadge.objects.get_or_create(badge_type="BRONZE",description="Question score of 10 or more", tag_name="Nice Question",date=timezone.now(),preBuild=True, bade_position="Tag", url="#")
    TagBadge.objects.get_or_create(badge_type="SILVER",description="Question score of 25 or more", tag_name="Good Question",date=timezone.now(),preBuild=True, bade_position="Tag", url="#")
    TagBadge.objects.get_or_create(badge_type="GOLD",description="Question score of 100 or more", tag_name="Great Question",date=timezone.now(),preBuild=True, bade_position="Tag", url="#")
    TagBadge.objects.get_or_create(badge_type="BRONZE",description="Question with 1,000 views", tag_name="Popular Question",date=timezone.now(),preBuild=True, bade_position="Tag", url="#")
    TagBadge.objects.get_or_create(badge_type="SILVER",description="Question with 2,500 views", tag_name="Notable Question",date=timezone.now(),preBuild=True, bade_position="Tag", url="#")
    TagBadge.objects.get_or_create(badge_type="GOLD",description="Question with 10,000 views", tag_name="Famous Question",date=timezone.now(),preBuild=True, bade_position="Tag", url="#")
    TagBadge.objects.get_or_create(badge_type="BRONZE",description="First bounty you offer on your own question", tag_name="Promoter",date=timezone.now(),preBuild=True, bade_position="Tag", url="#")
    TagBadge.objects.get_or_create(badge_type="BRONZE",description="Ask a question and accept an answer", tag_name="Scholar",date=timezone.now(),preBuild=True, bade_position="Tag", url="#")
    TagBadge.objects.get_or_create(badge_type="BRONZE",description="First question with score of 1 or more", tag_name="Student",date=timezone.now(),preBuild=True, bade_position="Tag", url="#")
    TagBadge.objects.get_or_create(badge_type="SILVER",description="First to answer and accepted with score of 10 or more", tag_name="Enlightened",date=timezone.now(),preBuild=True, bade_position="Tag", url="#")
    TagBadge.objects.get_or_create(badge_type="BRONZE",description="Edit and answer 1 question (both actions within 12 hours, answer score > 0)", tag_name="Explainer",date=timezone.now(),preBuild=True, bade_position="Tag", url="#")
    TagBadge.objects.get_or_create(badge_type="SILVER",description="Edit and answer 50 questions (both actions within 12 hours, answer score > 0)", tag_name="Refiner",date=timezone.now(),preBuild=True, bade_position="Tag", url="#")
    TagBadge.objects.get_or_create(badge_type="GOLD",description="Edit and answer 500 questions (both actions within 12 hours, answer score > 0)", tag_name="Illuminator",date=timezone.now(),preBuild=True, bade_position="Tag", url="#")
    TagBadge.objects.get_or_create(badge_type="SILVER",description="Accepted answer and score of 40 or more", tag_name="Guru",date=timezone.now(),preBuild=True, bade_position="Tag", url="#")
    TagBadge.objects.get_or_create(badge_type="SILVER",description="Answer score of 5 or more to a question score of -2 or less that goes on to receive a score of 2 or more", tag_name="Lifejacket",date=timezone.now(),preBuild=True, bade_position="Tag", url="#")
    TagBadge.objects.get_or_create(badge_type="GOLD",description="Answer score of 20 or more to a question score of -3 or less that goes on to receive a score of 3 or more", tag_name="Lifeboat",date=timezone.now(),preBuild=True, bade_position="Tag", url="#")
    TagBadge.objects.get_or_create(badge_type="BRONZE",description="Answer score of 10 or more", tag_name="Nice Answer",date=timezone.now(),preBuild=True, bade_position="Tag", url="#")
    TagBadge.objects.get_or_create(badge_type="SILVER",description="Answer score of 25 or more", tag_name="Good Answer",date=timezone.now(),preBuild=True, bade_position="Tag", url="#")
    TagBadge.objects.get_or_create(badge_type="GOLD",description="Answer score of 100 or more", tag_name="Great Answer",date=timezone.now(),preBuild=True, bade_position="Tag", url="#")
    # TagBadge.objects.get_or_create(badge_type="GOLD", tag_name="Populist",date=timezone.now(),preBuild=True, bade_position="Tag", url="#")
    TagBadge.objects.get_or_create(badge_type="BRONZE",description="Answer more than 30 days after a question was asked as first answer scoring 2 or more", tag_name="Revival",date=timezone.now(),preBuild=True, bade_position="Tag", url="#")
    TagBadge.objects.get_or_create(badge_type="SILVER",description="Answer a question more than 60 days later with score of 5 or more", tag_name="Necromancer",date=timezone.now(),preBuild=True, bade_position="Tag", url="#")
    TagBadge.objects.get_or_create(badge_type="BRONZE",description="Answer your own question with score of 3 or more", tag_name="Self-Learner",date=timezone.now(),preBuild=True, bade_position="Tag", url="#")
    TagBadge.objects.get_or_create(badge_type="BRONZE",description="Answer a question with score of 1 or more", tag_name="Teacher",date=timezone.now(),preBuild=True, bade_position="Tag", url="#")
    # TagBadge.objects.get_or_create(badge_type="SILVER", tag_name="Tanacious",date=timezone.now(),preBuild=True, bade_position="Tag", url="#")
    # TagBadge.objects.get_or_create(badge_type="GOLD", tag_name="Unsung Hero",date=timezone.now(),preBuild=True, bade_position="Tag", url="#")
    TagBadge.objects.get_or_create(badge_type="BRONZE",description="Complete 'About Me' section of user profile", tag_name="Autobiographer",date=timezone.now(),preBuild=True, bade_position="Tag", url="#")
    TagBadge.objects.get_or_create(badge_type="BRONZE",description="Leave 10 comments", tag_name="Commentator",date=timezone.now(),preBuild=True, bade_position="Tag", url="#")
    TagBadge.objects.get_or_create(badge_type="GOLD",description="Leave 10 comments with score of 5 or more", tag_name="Pundit",date=timezone.now(),preBuild=True, bade_position="Tag", url="#")
    # TagBadge.objects.get_or_create(badge_type="BRONZE", tag_name="Mortarboard",date=timezone.now(),preBuild=True, bade_position="Tag", url="#")
    TagBadge.objects.get_or_create(badge_type="SILVER",description="Earn 200 daily reputation 50 times", tag_name="Epic",date=timezone.now(),preBuild=True, bade_position="Tag", url="#")
    TagBadge.objects.get_or_create(badge_type="GOLD",description="Earn 200 daily reputation 150 times", tag_name="Legendary",date=timezone.now(),preBuild=True, bade_position="Tag", url="#")
    # TagBadge.objects.get_or_create(badge_type="BRONZE", tag_name="Bronze Badge",date=timezone.now(),preBuild=True, bade_position="Tag", url="#")
    # TagBadge.objects.get_or_create(badge_type="SILVER", tag_name="Silver Badge",date=timezone.now(),preBuild=True, bade_position="Tag", url="#")
    # TagBadge.objects.get_or_create(badge_type="GOLD", tag_name="Gold Badge",date=timezone.now(),preBuild=True, bade_position="Tag", url="#")
    TagBadge.objects.get_or_create(badge_type="BRONZE",description="First flagged post", tag_name="Citizen Patrol",date=timezone.now(),preBuild=True, bade_position="Tag", url="#")
    TagBadge.objects.get_or_create(badge_type="SILVER",description="Raise 80 helpful flags", tag_name="Deputy",date=timezone.now(),preBuild=True, bade_position="Tag", url="#")
    TagBadge.objects.get_or_create(badge_type="GOLD",description="Raise 500 helpful flags", tag_name="Marshal",date=timezone.now(),preBuild=True, bade_position="Tag", url="#")
    TagBadge.objects.get_or_create(badge_type="SILVER",description="Vote 300 or more times", tag_name="Civic Duty",date=timezone.now(),preBuild=True, bade_position="Tag", url="#")
    TagBadge.objects.get_or_create(badge_type="BRONZE",description="First down vote", tag_name="Critic",date=timezone.now(),preBuild=True, bade_position="Tag", url="#")
    TagBadge.objects.get_or_create(badge_type="BRONZE",description="Complete at least one review task. This badge is awarded once per review type", tag_name="Custodian",date=timezone.now(),preBuild=True, bade_position="Tag", url="#")
    TagBadge.objects.get_or_create(badge_type="SILVER",description="Complete at least 250 review tasks. This badge is awarded once per review type", tag_name="Reviewer",date=timezone.now(),preBuild=True, bade_position="Tag", url="#")
    TagBadge.objects.get_or_create(badge_type="GOLD",description="Complete at least 1,000 review tasks. This badge is awarded multiple times per review type", tag_name="Steward",date=timezone.now(),preBuild=True, bade_position="Tag", url="#")
    TagBadge.objects.get_or_create(badge_type="BRONZE",description="Delete own post with score of 3 or higher", tag_name="Disciplined",date=timezone.now(),preBuild=True, bade_position="Tag", url="#")
    TagBadge.objects.get_or_create(badge_type="BRONZE",description="First edit", tag_name="Editor",date=timezone.now(),preBuild=True, bade_position="Tag", url="#")
    TagBadge.objects.get_or_create(badge_type="SILVER",description="Edit 80 posts", tag_name="Strunk & White",date=timezone.now(),preBuild=True, bade_position="Tag", url="#")
    TagBadge.objects.get_or_create(badge_type="GOLD",description="Edit 500 posts (excluding own or deleted posts and tag edits)", tag_name="Copy Editor",date=timezone.now(),preBuild=True, bade_position="Tag", url="#")
    # TagBadge.objects.get_or_create(badge_type="GOLD",description="Edit 500 posts (excluding own or deleted posts and tag edits)", tag_name="Electorate",date=timezone.now(),preBuild=True, bade_position="Tag", url="#")
    TagBadge.objects.get_or_create(badge_type="BRONZE",description="Edit first post that was inactive for 6 months", tag_name="Excavator",date=timezone.now(),preBuild=True, bade_position="Tag", url="#")
    TagBadge.objects.get_or_create(badge_type="SILVER",description="Edit 100 posts that were inactive for 6 months", tag_name="Archaologist",date=timezone.now(),preBuild=True, bade_position="Tag", url="#")
    TagBadge.objects.get_or_create(badge_type="BRONZE",description="Delete own post with score of -3 or lower", tag_name="Peer Pressure",date=timezone.now(),preBuild=True, bade_position="Tag", url="#")
    TagBadge.objects.get_or_create(badge_type="BRONZE",description="Approve or reject 100 suggested edits", tag_name="Proodreader",date=timezone.now(),preBuild=True, bade_position="Tag", url="#")
    # TagBadge.objects.get_or_create(badge_type="SILVER", tag_name="Sportsmanship",date=timezone.now(),preBuild=True, bade_position="Tag", url="#")
    TagBadge.objects.get_or_create(badge_type="BRONZE",description="Use 30 votes in a day", tag_name="Suffrage",date=timezone.now(),preBuild=True, bade_position="Tag", url="#")
    TagBadge.objects.get_or_create(badge_type="BRONZE",description="First up vote", tag_name="Supporter",date=timezone.now(),preBuild=True, bade_position="Tag", url="#")
    TagBadge.objects.get_or_create(badge_type="GOLD",description="Provide an answer of +20 score to a question of -5 score", tag_name="Reversal",date=timezone.now(),preBuild=True, bade_position="Tag", url="#")
    # TagBadge.objects.get_or_create(badge_type="BRONZE", tag_name="Tubbleweed",date=timezone.now(),preBuild=True, bade_position="Tag", url="#")
    TagBadge.objects.get_or_create(badge_type="BRONZE",description="Use the maximum 40 votes in a day", tag_name="Vox Populi",date=timezone.now(),preBuild=True, bade_position="Tag", url="#")
    TagBadge.objects.get_or_create(badge_type="BRONZE",description="Read the entire tour page", tag_name="Informed",date=timezone.now(),preBuild=True, bade_position="Tag", url="#")



def saveTag(apps, schema_editor):
    Tag = apps.get_model("taggit", "Tag")
    Tag.objects.get_or_create(name="Altruist", slug="altruist")
    Tag.objects.get_or_create(name="Benefactor", slug="benefactor")
    Tag.objects.get_or_create(name="Favorite Question", slug="favorite-question")
    Tag.objects.get_or_create(name="Stellar Question", slug="stellar-question")
    Tag.objects.get_or_create(name="Investor", slug="investor")
    Tag.objects.get_or_create(name="Nice Question", slug="nice-question")
    Tag.objects.get_or_create(name="Good Question", slug="good-question")
    Tag.objects.get_or_create(name="Great Question", slug="great-question")
    Tag.objects.get_or_create(name="Popular Question", slug="popular-question")
    Tag.objects.get_or_create(name="Notable Question", slug="notable-question")
    Tag.objects.get_or_create(name="Famous Question", slug="famous-question")
    Tag.objects.get_or_create(name="Promoter", slug="promoter")
    Tag.objects.get_or_create(name="Scholar", slug="scholar")
    Tag.objects.get_or_create(name="Student", slug="student")
    Tag.objects.get_or_create(name="Enlightened", slug="enlightened")
    Tag.objects.get_or_create(name="Explainer", slug="explainer")
    Tag.objects.get_or_create(name="Refiner", slug="refiner")
    Tag.objects.get_or_create(name="Illuminator", slug="illuminator")
    Tag.objects.get_or_create(name="Guru", slug="guru")
    Tag.objects.get_or_create(name="Lifejacket", slug="lifejacket")
    Tag.objects.get_or_create(name="Lifeboat", slug="lifeboat")
    Tag.objects.get_or_create(name="Nice Answer", slug="nice-answer")
    Tag.objects.get_or_create(name="Good Answer", slug="good-answer")
    Tag.objects.get_or_create(name="Great Answer", slug="great-answer")
    # Tag.objects.get_or_create(name="Populist", slug="populist")
    Tag.objects.get_or_create(name="Revival", slug="revival")
    Tag.objects.get_or_create(name="Necromancer", slug="necromancer")
    Tag.objects.get_or_create(name="Self-Learner", slug="self-learner")
    Tag.objects.get_or_create(name="Teacher", slug="teacher")
    # Tag.objects.get_or_create(name="Tanacious", slug="tanacious")
    # Tag.objects.get_or_create(name="Unsung Hero", slug="unsung-hero")
    Tag.objects.get_or_create(name="Autobiographer", slug="autobiographer")
    Tag.objects.get_or_create(name="Commentator", slug="commentator")
    Tag.objects.get_or_create(name="Pundit", slug="pundit")
    Tag.objects.get_or_create(name="Mortarboard", slug="mortarboard")
    Tag.objects.get_or_create(name="Epic", slug="epic")
    Tag.objects.get_or_create(name="Legendary", slug="legendary")
    # Tag.objects.get_or_create(name="Bronze Badge", slug="bronze-badge")
    # Tag.objects.get_or_create(name="Silver Badge", slug="silver-badge")
    # Tag.objects.get_or_create(name="Gold Badge", slug="gold-badge")
    Tag.objects.get_or_create(name="Citizen Patrol", slug="citizen-patrol")
    Tag.objects.get_or_create(name="Deputy", slug="deputy")
    Tag.objects.get_or_create(name="Marshal", slug="marshal")
    Tag.objects.get_or_create(name="Civic Duty", slug="civic-duty")
    Tag.objects.get_or_create(name="Critic", slug="critic")
    Tag.objects.get_or_create(name="Custodian", slug="custodian")
    Tag.objects.get_or_create(name="Reviewer", slug="reviewer")
    Tag.objects.get_or_create(name="Steward", slug="steward")
    Tag.objects.get_or_create(name="Disciplined", slug="disciplined")
    Tag.objects.get_or_create(name="Edit", slug="edit")
    Tag.objects.get_or_create(name="Strunk & White", slug="strunk-&-white")
    Tag.objects.get_or_create(name="Copy Editor", slug="copy-editor")
    Tag.objects.get_or_create(name="Electorate", slug="electorate")
    Tag.objects.get_or_create(name="Excavator", slug="excavator")
    Tag.objects.get_or_create(name="Archaologist", slug="archaologist")
    Tag.objects.get_or_create(name="Peer Pressure", slug="peer-pressure")
    Tag.objects.get_or_create(name="Proodreader", slug="proodreader")
    # Tag.objects.get_or_create(name="Sportsmanship", slug="sportsmanship")
    Tag.objects.get_or_create(name="Suffrage", slug="suffrage")
    Tag.objects.get_or_create(name="Supporter", slug="supporter")
    Tag.objects.get_or_create(name="Reversal", slug="reversal")
    # Tag.objects.get_or_create(name="Tubbleweed", slug="tubbleweed")
    Tag.objects.get_or_create(name="Vox Populi", slug="vox-populi")
    Tag.objects.get_or_create(name="Informed", slug="informed")


class Migration(migrations.Migration):

    dependencies = [
        ('tagbadge', '0003_auto_20220105_1219'),
    ]

    operations = [
        migrations.RunPython(saveTag),
        migrations.RunPython(saveTagBadge)
    ]