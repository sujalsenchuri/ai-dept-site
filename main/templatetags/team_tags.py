from django import template
from django.utils.html import mark_safe
from main.models import TeamMember, ServiceCard
from urllib.parse import urlparse

register = template.Library()


@register.inclusion_tag('team_card.html')
def team_member_card(member):
    """Render a single team member card."""
    return {'member': member}


@register.simple_tag
def load_team_members():
    """Return all team members from database."""
    return TeamMember.objects.all()


@register.simple_tag
def load_service_cards():
    """Return the 3 most recent service cards from database."""
    return ServiceCard.objects.all()[:3]



@register.simple_tag
def load_all_service_cards():
    """Return all service cards (used on news page)."""
    return ServiceCard.objects.all()


@register.filter
def normalize_club_link(value):
    """Normalize club links so local templates resolve to /page.html."""
    if not value:
        return value

    raw = str(value).strip()
    parsed = urlparse(raw)

    # Convert malformed internal http://aipc.html to /aipc.html
    if parsed.scheme in {'http', 'https'} and parsed.netloc and parsed.netloc.endswith('.html') and not parsed.path:
        return '/' + parsed.netloc

    # Convert relative template names like aipc.html to /aipc.html
    if not parsed.scheme and not raw.startswith('/'):
        return '/' + raw

    return raw
