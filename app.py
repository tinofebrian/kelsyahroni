from flask import Flask, render_template, abort

app = Flask(__name__)

# Data untuk 5 Anggota Tim Anda
team_members = [
    {
        'id': 1,
        'name': 'HASBI',
        'nim': '23.83.1018',
        'role': 'PROJECT LEAD & DEVOPS',
        'image': 'member1.jpg',
        'description': 'Bertanggung jawab atas arsitektur proyek di Azure App Service dan integrasi CI/CD.'
    },
    {
        'id': 2,
        'name': 'DITO',
        'nim': '23.83.1032',
        'role': 'BACKEND DEVELOPER',
        'image': 'member2.jpg',
        'description': 'Fokus pada pengembangan logika aplikasi menggunakan Flask, dan integrasi API layanan Azure.'
    },
    {
        'id': 3,
        'name': 'FEBRIO',
        'nim': '23.83.1009',
        'role': 'FRONTEND DEVELOPER (UI/UX)',
        'image': 'member3.jpg',
        'description': 'Mendesain antarmuka pengguna yang responsif dan implementasi interaksi.'
    },
    {
        'id': 4,
        'name': 'BANI',
        'nim': '23.83.1046',
        'role': 'CLOUD SECURITY SPECIALIST',
        'image': 'member4.jpg',
        'description': 'Mengawasi keamanan aplikasi, memastikan konfigurasi Azure mengikuti praktik terbaik keamanan.'
    },
    {
        'id': 5,
        'name': 'BRIAN',
        'nim': '23.83.1048',
        'role': 'QUALITY ASSURANCE (QA)',
        'image': 'member5.jpg',
        'description': 'Melakukan pengujian fungsionalitas dan non-fungsionalitas aplikasi.'
    }
]

# Route default: menampilkan anggota pertama
@app.route('/')
def index():
    # Arahkan ke profil anggota pertama secara default
    return render_template('index.html', 
                           members=team_members,
                           active_member=team_members[0])

# Route untuk menampilkan detail anggota berdasarkan ID
@app.route('/member/<int:member_id>')
def member_profile(member_id):
    member = next((m for m in team_members if m['id'] == member_id), None)
    if member is None:
        abort(404) # Tampilkan error 404 jika anggota tidak ditemukan
    
    return render_template('index.html', 
                           members=team_members, 
                           active_member=member)

if __name__ == '__main__':
    app.run(debug=True)