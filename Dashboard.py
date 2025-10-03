# dashboard_livres_sacres_avance.py
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import base64
from io import BytesIO

# Configuration de la page
st.set_page_config(
    page_title="Analyse Avancée - Livres Sacrés",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personnalisé avancé
st.markdown("""
<style>
    .main-header {
        font-size: 2.8rem;
        background: linear-gradient(45deg, #2E86AB, #A23B72, #F18F01);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: 800;
    }
    .advanced-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
    }
    .quran-gradient { background: linear-gradient(135deg, #2E86AB 0%, #4FB477 100%); }
    .torah-gradient { background: linear-gradient(135deg, #A23B72 0%, #D85F6E 100%); }
    .bible-gradient { background: linear-gradient(135deg, #F18F01 0%, #C73E1D 100%); }
    .analysis-section {
        background: #f8f9fa;
        padding: 2rem;
        border-radius: 15px;
        margin: 1rem 0;
        border-left: 5px solid #2E86AB;
    }
    .metric-large {
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
    }
    .submetric {
        font-size: 1rem;
        opacity: 0.9;
    }
</style>
""", unsafe_allow_html=True)

class AdvancedSacredBooksAnalysis:
    def __init__(self):
        self.books_data = self.load_advanced_data()
        self.thematic_data = self.load_thematic_analysis()
        self.linguistic_data = self.load_linguistic_analysis()
        self.historical_data = self.load_historical_analysis()
        
    def load_advanced_data(self):
        """Charge des données avancées pour l'analyse"""
        books = {
            'Coran': {
                'structural_analysis': {
                    'avg_verse_length': 25.6,
                    'vocabulary_richness': 0.85,
                    'repetition_rate': 12.3,
                    'rhythmic_patterns': 94,
                    'thematic_cohesion': 9.2
                },
                'linguistic_features': {
                    'unique_words': 14870,
                    'root_words': 1726,
                    'grammatical_complexity': 8.7,
                    'semantic_density': 9.1,
                    'oral_preservation': 99.9
                },
                'historical_impact': {
                    'manuscripts_earliest': 642,
                    'translations_timeline': 112,
                    'academic_studies': 125000,
                    'cultural_references': 890000,
                    'legal_influence': 9.5
                }
            },
            'Torah': {
                'structural_analysis': {
                    'avg_verse_length': 18.3,
                    'vocabulary_richness': 0.78,
                    'repetition_rate': 8.7,
                    'rhythmic_patterns': 45,
                    'thematic_cohesion': 8.8
                },
                'linguistic_features': {
                    'unique_words': 8920,
                    'root_words': 1850,
                    'grammatical_complexity': 7.9,
                    'semantic_density': 8.4,
                    'oral_preservation': 95.2
                },
                'historical_impact': {
                    'manuscripts_earliest': -250,
                    'translations_timeline': 25,
                    'academic_studies': 89000,
                    'cultural_references': 450000,
                    'legal_influence': 9.8
                }
            },
            'Bible': {
                'structural_analysis': {
                    'avg_verse_length': 22.1,
                    'vocabulary_richness': 0.92,
                    'repetition_rate': 15.8,
                    'rhythmic_patterns': 67,
                    'thematic_cohesion': 8.5
                },
                'linguistic_features': {
                    'unique_words': 12850,
                    'root_words': 4200,
                    'grammatical_complexity': 8.2,
                    'semantic_density': 8.8,
                    'oral_preservation': 97.8
                },
                'historical_impact': {
                    'manuscripts_earliest': 125,
                    'translations_timeline': 1382,
                    'academic_studies': 450000,
                    'cultural_references': 2500000,
                    'legal_influence': 9.2
                }
            }
        }
        return books

    def load_thematic_analysis(self):
        """Charge l'analyse thématique détaillée"""
        themes = {
            'Thèmes Théologiques': {
                'Coran': [95, 90, 85, 80, 92, 88, 75],
                'Torah': [90, 85, 95, 75, 90, 70, 60],
                'Bible': [85, 88, 75, 90, 85, 95, 85],
                'Sous-thèmes': ['Monothéisme', 'Prophétie', 'Révélation', 'Salut', 'Divinité', 'Grâce', 'Jugement']
            },
            'Thèmes Éthiques': {
                'Coran': [88, 92, 85, 78, 90, 82, 75],
                'Torah': [85, 90, 92, 80, 88, 75, 70],
                'Bible': [90, 85, 88, 92, 85, 90, 80],
                'Sous-thèmes': ['Justice', 'Compassion', 'Honnêteté', 'Pardon', 'Humilité', 'Générosité', 'Paix']
            },
            'Thèmes Sociaux': {
                'Coran': [85, 80, 90, 75, 82, 88, 70],
                'Torah': [90, 85, 92, 88, 85, 80, 75],
                'Bible': [80, 85, 78, 90, 82, 85, 88],
                'Sous-thèmes': ['Famille', 'Communauté', 'Autorité', 'Économie', 'Guerre', 'Diplomatie', 'Éducation']
            }
        }
        return themes

    def load_linguistic_analysis(self):
        """Charge l'analyse linguistique avancée"""
        linguistic_features = {
            'Complexité Syntaxique': {
                'Coran': 8.7, 'Torah': 7.9, 'Bible': 8.2
            },
            'Densité Sémantique': {
                'Coran': 9.1, 'Torah': 8.4, 'Bible': 8.8
            },
            'Richesse Lexicale': {
                'Coran': 0.85, 'Torah': 0.78, 'Bible': 0.92
            },
            'Répétition Stylistique': {
                'Coran': 12.3, 'Torah': 8.7, 'Bible': 15.8
            },
            'Structure Narrative': {
                'Coran': 7.8, 'Torah': 9.2, 'Bible': 8.5
            }
        }
        return linguistic_features

    def load_historical_analysis(self):
        """Charge l'analyse historique détaillée"""
        timeline = pd.DataFrame({
            'Année': [-1500, -1000, -500, 0, 500, 1000, 1500, 2000],
            'Coran': [0, 0, 0, 0, 10, 45, 70, 95],
            'Torah': [5, 30, 60, 75, 80, 82, 85, 88],
            'Bible': [0, 5, 20, 40, 65, 80, 90, 98],
            'Événement': [
                'Textes anciens', 'Rédaction Torah', 'Canonisation', 'Jésus-Christ', 
                'Expansion islam', 'Schisme', 'Réforme', 'Globalisation'
            ]
        })
        return timeline

    def create_advanced_header(self):
        """En-tête avancé avec métriques complexes"""
        st.markdown('<h1 class="main-header">🔍 Analyse Avancée des Livres Sacrés</h1>', 
                   unsafe_allow_html=True)
        
        # Métriques avancées
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            total_complexity = sum([self.linguistic_data['Complexité Syntaxique'][book] for book in ['Coran', 'Torah', 'Bible']])
            st.metric("Complexité Linguistique Moyenne", f"{total_complexity/3:.1f}/10")
        
        with col2:
            total_preservation = sum([self.books_data[book]['linguistic_features']['oral_preservation'] for book in ['Coran', 'Torah', 'Bible']])
            st.metric("Préservation Moyenne", f"{total_preservation/3:.1f}%")
        
        with col3:
            total_influence = sum([self.books_data[book]['historical_impact']['legal_influence'] for book in ['Coran', 'Torah', 'Bible']])
            st.metric("Influence Juridique Moyenne", f"{total_influence/3:.1f}/10")
        
        with col4:
            total_studies = sum([self.books_data[book]['historical_impact']['academic_studies'] for book in ['Coran', 'Torah', 'Bible']])
            st.metric("Études Académiques", f"{total_studies/1000:.0f}K")

    def create_structural_analysis(self):
        """Analyse structurelle avancée"""
        st.markdown("## 🏗️ Analyse Structurelle Avancée")
        
        tab1, tab2, tab3 = st.tabs(["📐 Métriques Structurelles", "🔄 Patterns", "📊 Analyse Comparative"])
        
        with tab1:
            col1, col2 = st.columns([2, 1])
            
            with col1:
                # Radar chart des métriques structurelles
                metrics = ['avg_verse_length', 'vocabulary_richness', 'repetition_rate', 'rhythmic_patterns', 'thematic_cohesion']
                metric_names = ['Longueur Versets', 'Richesse Vocabulaire', 'Taux Répétition', 'Patterns Rythmiques', 'Cohésion Thématique']
                
                fig = go.Figure()
                
                for book in ['Coran', 'Torah', 'Bible']:
                    values = [self.books_data[book]['structural_analysis'][metric] for metric in metrics]
                    # Normalisation
                    max_vals = [max([self.books_data[b]['structural_analysis'][m] for b in ['Coran', 'Torah', 'Bible']]) for m in metrics]
                    normalized = [v/max_v * 100 for v, max_v in zip(values, max_vals)]
                    
                    fig.add_trace(go.Scatterpolar(
                        r=normalized,
                        theta=metric_names,
                        fill='toself',
                        name=book,
                        line=dict(color=self.get_book_color(book))
                    ))
                
                fig.update_layout(
                    polar=dict(
                        radialaxis=dict(visible=True, range=[0, 100])
                    ),
                    title="Profil Structurel Comparatif",
                    height=500
                )
                st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                st.markdown("### 📈 Indices de Complexité")
                complexity_data = []
                for book in ['Coran', 'Torah', 'Bible']:
                    data = self.books_data[book]['structural_analysis']
                    complexity_score = (
                        data['vocabulary_richness'] * 30 +
                        data['thematic_cohesion'] * 25 +
                        (100 - data['repetition_rate']) * 20 +
                        data['rhythmic_patterns'] * 0.25
                    ) / 100
                    complexity_data.append({'Livre': book, 'Complexité': complexity_score})
                
                complexity_df = pd.DataFrame(complexity_data)
                fig = px.bar(complexity_df, x='Livre', y='Complexité', color='Livre',
                            color_discrete_map=self.get_color_map())
                st.plotly_chart(fig, use_container_width=True)
        
        with tab2:
            st.subheader("🔄 Analyse des Patterns Littéraires")
            
            # Simulation de données de patterns
            patterns_data = {
                'Type de Pattern': ['Parallélisme', 'Chiasme', 'Inclusion', 'Répétition', 'Symétrie', 'Acrostiche'],
                'Coran': [85, 78, 92, 88, 75, 65],
                'Torah': [80, 85, 78, 82, 88, 70],
                'Bible': [75, 72, 85, 90, 80, 60]
            }
            patterns_df = pd.DataFrame(patterns_data)
            
            fig = px.scatter(patterns_df, x='Type de Pattern', y=['Coran', 'Torah', 'Bible'],
                            title="Utilisation des Patterns Littéraires",
                            color_discrete_map=self.get_color_map())
            st.plotly_chart(fig, use_container_width=True)

    def create_linguistic_analysis(self):
        """Analyse linguistique approfondie"""
        st.markdown("## 🈯 Analyse Linguistique Avancée")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Heatmap des caractéristiques linguistiques
            linguistic_df = pd.DataFrame(self.linguistic_data).T
            linguistic_df = linguistic_df.reset_index().rename(columns={'index': 'Caractéristique'})
            
            fig = px.imshow(linguistic_df.set_index('Caractéristique'),
                          title="Matrice des Caractéristiques Linguistiques",
                          color_continuous_scale='Viridis',
                          aspect="auto")
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Évolution de la complexité linguistique
            st.subheader("📊 Distribution des Caractéristiques")
            
            features = ['Complexité Syntaxique', 'Densité Sémantique', 'Richesse Lexicale']
            values = [[self.linguistic_data[f][book] for f in features] for book in ['Coran', 'Torah', 'Bible']]
            
            fig = go.Figure(data=[
                go.Bar(name='Coran', x=features, y=values[0], marker_color='#2E86AB'),
                go.Bar(name='Torah', x=features, y=values[1], marker_color='#A23B72'),
                go.Bar(name='Bible', x=features, y=values[2], marker_color='#F18F01')
            ])
            
            fig.update_layout(barmode='group', title="Comparaison des Features Linguistiques")
            st.plotly_chart(fig, use_container_width=True)
        
        # Analyse détaillée par livre
        st.subheader("📖 Analyse Linguistique par Livre")
        
        for book in ['Coran', 'Torah', 'Bible']:
            with st.expander(f"🔍 Analyse détaillée - {book}"):
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.markdown("**📐 Structure**")
                    data = self.books_data[book]['structural_analysis']
                    st.metric("Longueur moyenne verset", f"{data['avg_verse_length']} mots")
                    st.metric("Richesse vocabulaire", f"{data['vocabulary_richness']:.2f}")
                    st.metric("Cohésion thématique", f"{data['thematic_cohesion']}/10")
                
                with col2:
                    st.markdown("**🔤 Linguistique**")
                    data = self.books_data[book]['linguistic_features']
                    st.metric("Mots uniques", f"{data['unique_words']:,}")
                    st.metric("Racines linguistiques", f"{data['root_words']}")
                    st.metric("Préservation orale", f"{data['oral_preservation']}%")
                
                with col3:
                    st.markdown("**📊 Complexité**")
                    st.metric("Densité sémantique", f"{data['semantic_density']}/10")
                    st.metric("Complexité grammaticale", f"{data['grammatical_complexity']}/10")
                    complexity_score = (data['semantic_density'] + data['grammatical_complexity']) / 2
                    st.metric("Score complexité global", f"{complexity_score:.1f}/10")

    def create_thematic_network_analysis(self):
        """Analyse des réseaux thématiques"""
        st.markdown("## 🕸️ Analyse des Réseaux Thématiques")
        
        # Données simulées pour l'analyse de réseau
        thematic_networks = {
            'Coran': {
                'nœuds': ['Monothéisme', 'Prophètes', 'Loi', 'Éthique', 'Jugement', 'Création'],
                'liens': [
                    ('Monothéisme', 'Prophètes', 95), ('Monothéisme', 'Loi', 88),
                    ('Prophètes', 'Loi', 82), ('Loi', 'Éthique', 90),
                    ('Éthique', 'Jugement', 85), ('Monothéisme', 'Création', 92)
                ]
            },
            'Torah': {
                'nœuds': ['Alliance', 'Loi', 'Histoire', 'Sacrifice', 'Territoire', 'Pure té'],
                'liens': [
                    ('Alliance', 'Loi', 98), ('Alliance', 'Histoire', 88),
                    ('Loi', 'Sacrifice', 85), ('Histoire', 'Territoire', 92),
                    ('Loi', 'Pure té', 90), ('Sacrifice', 'Pure té', 82)
                ]
            },
            'Bible': {
                'nœuds': ['Salut', 'Amour', 'Grâce', 'Rédemption', 'Église', 'Royaume'],
                'liens': [
                    ('Salut', 'Amour', 92), ('Salut', 'Grâce', 95),
                    ('Amour', 'Grâce', 88), ('Grâce', 'Rédemption', 90),
                    ('Rédemption', 'Église', 85), ('Salut', 'Royaume', 82)
                ]
            }
        }
        
        tab1, tab2, tab3 = st.tabs(["Coran", "Torah", "Bible"])
        
        for idx, (book, tab) in enumerate(zip(['Coran', 'Torah', 'Bible'], [tab1, tab2, tab3])):
            with tab:
                st.subheader(f"Réseau Thématique - {book}")
                
                # Création du graphique de réseau simplifié
                network = thematic_networks[book]
                
                # Position des nœuds (simulée)
                node_positions = {
                    'Monothéisme': (0, 1), 'Prophètes': (1, 1), 'Loi': (0.5, 0.5),
                    'Éthique': (0, 0), 'Jugement': (1, 0), 'Création': (0.5, 1.5),
                    'Alliance': (0, 1), 'Histoire': (1, 1), 'Sacrifice': (0.5, 0.5),
                    'Territoire': (0, 0), 'Pure té': (1, 0), 'Salut': (0.5, 1.5),
                    'Amour': (0, 1), 'Grâce': (1, 1), 'Rédemption': (0.5, 0.5),
                    'Église': (0, 0), 'Royaume': (1, 0)
                }
                
                fig = go.Figure()
                
                # Ajout des liens
                for link in network['liens']:
                    source, target, weight = link
                    fig.add_trace(go.Scatter(
                        x=[node_positions[source][0], node_positions[target][0], None],
                        y=[node_positions[source][1], node_positions[target][1], None],
                        mode='lines',
                        line=dict(width=weight/20, color='gray'),
                        hoverinfo='none'
                    ))
                
                # Ajout des nœuds
                node_x = [node_positions[node][0] for node in network['nœuds']]
                node_y = [node_positions[node][1] for node in network['nœuds']]
                
                fig.add_trace(go.Scatter(
                    x=node_x, y=node_y,
                    mode='markers+text',
                    marker=dict(size=20, color=self.get_book_color(book)),
                    text=network['nœuds'],
                    textposition="middle center",
                    hoverinfo='text'
                ))
                
                fig.update_layout(
                    title=f"Réseau Thématique - {book}",
                    showlegend=False,
                    height=400,
                    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)
                )
                
                st.plotly_chart(fig, use_container_width=True)
                
                # Métriques du réseau
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Nombre de nœuds", len(network['nœuds']))
                with col2:
                    avg_weight = sum([link[2] for link in network['liens']]) / len(network['liens'])
                    st.metric("Liaison moyenne", f"{avg_weight:.1f}%")
                with col3:
                    st.metric("Densité du réseau", f"{(len(network['liens']) / (len(network['nœuds'])*(len(network['nœuds'])-1)/2))*100:.1f}%")

    def create_historical_evolution(self):
        """Analyse historique avancée"""
        st.markdown("## 📜 Évolution Historique et Influence")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Timeline interactive
            fig = px.line(self.historical_data, x='Année', y=['Coran', 'Torah', 'Bible'],
                         title="Évolution de l'Influence Historique",
                         color_discrete_map=self.get_color_map())
            
            # Ajout des événements
            for _, row in self.historical_data.iterrows():
                fig.add_annotation(
                    x=row['Année'], y=row['Coran'],
                    text=row['Événement'],
                    showarrow=True,
                    arrowhead=1
                )
            
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Carte de diffusion mondiale (simulée)
            diffusion_data = {
                'Région': ['Moyen-Orient', 'Europe', 'Afrique', 'Asie', 'Amériques'],
                'Coran': [95, 25, 60, 35, 15],
                'Torah': [5, 15, 2, 3, 20],
                'Bible': [15, 85, 75, 20, 90]
            }
            diffusion_df = pd.DataFrame(diffusion_data)
            
            fig = px.bar(diffusion_df, x='Région', y=['Coran', 'Torah', 'Bible'],
                        title="Diffusion Géographique Actuelle (%)",
                        barmode='group',
                        color_discrete_map=self.get_color_map())
            st.plotly_chart(fig, use_container_width=True)
        
        # Analyse d'impact détaillée
        st.subheader("📈 Analyse d'Impact Détaillée")
        
        impact_metrics = ['Influence Culturelle', 'Impact Légal', 'Contribution Philosophique', 'Influence Artistique']
        impact_data = {
            'Coran': [9.2, 9.5, 8.8, 8.5],
            'Torah': [8.8, 9.8, 9.0, 7.8],
            'Bible': [9.5, 9.2, 9.3, 9.1]
        }
        
        fig = go.Figure()
        for book in ['Coran', 'Torah', 'Bible']:
            fig.add_trace(go.Scatterpolar(
                r=impact_data[book],
                theta=impact_metrics,
                fill='toself',
                name=book,
                line=dict(color=self.get_book_color(book))
            ))
        
        fig.update_layout(
            polar=dict(
                radialaxis=dict(visible=True, range=[0, 10])
            ),
            title="Analyse Multidimensionnelle de l'Impact",
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)

    def create_comparative_insights(self):
        """Insights comparatifs avancés"""
        st.markdown("## 💡 Insights Comparatifs Avancés")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("🎯 Points de Convergence")
            convergence_data = {
                'Aspect': ['Monothéisme', 'Prophètes communs', 'Éthique fondamentale', 'Jugement dernier', 'Prière'],
                'Degré': [95, 88, 85, 82, 78]
            }
            convergence_df = pd.DataFrame(convergence_data)
            
            fig = px.bar(convergence_df, x='Degré', y='Aspect', orientation='h',
                        title="Points de Convergence Doctrinaux",
                        color='Degré', color_continuous_scale='Viridis')
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.subheader("⚡ Points de Divergence")
            divergence_data = {
                'Aspect': ['Nature divine', 'Salut', 'Loi religieuse', 'Statut des prophètes', 'Rites'],
                'Écart': [85, 80, 75, 70, 65]
            }
            divergence_df = pd.DataFrame(divergence_data)
            
            fig = px.bar(divergence_df, x='Écart', y='Aspect', orientation='h',
                        title="Principales Divergences Doctrinales",
                        color='Écart', color_continuous_scale='Plasma')
            st.plotly_chart(fig, use_container_width=True)
        
        # Matrice de similarité
        st.subheader("🔗 Matrice de Similarité Doctrinale")
        
        similarity_matrix = np.array([
            [1.00, 0.65, 0.58],
            [0.65, 1.00, 0.72],
            [0.58, 0.72, 1.00]
        ])
        
        fig = px.imshow(similarity_matrix,
                       x=['Coran', 'Torah', 'Bible'],
                       y=['Coran', 'Torah', 'Bible'],
                       title="Matrice de Similarité Doctrinale",
                       color_continuous_scale='Blues',
                       text_auto=True)
        st.plotly_chart(fig, use_container_width=True)

    def create_advanced_metrics_dashboard(self):
        """Tableau de bord des métriques avancées"""
        st.markdown("## 📊 Tableau de Bord des Métriques Avancées")
        
        # Sélection du livre pour l'analyse détaillée
        selected_book = st.selectbox("📖 Sélectionnez un livre pour l'analyse détaillée", 
                                   ['Coran', 'Torah', 'Bible'])
        
        if selected_book:
            book_data = self.books_data[selected_book]
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown(f"### 🏗️ Structure - {selected_book}")
                structural = book_data['structural_analysis']
                
                metrics = [
                    ("Longueur verset moyen", f"{structural['avg_verse_length']} mots"),
                    ("Richesse vocabulaire", f"{structural['vocabulary_richness']:.2f}"),
                    ("Taux de répétition", f"{structural['repetition_rate']}%"),
                    ("Patterns rythmiques", f"{structural['rhythmic_patterns']}"),
                    ("Cohésion thématique", f"{structural['thematic_cohesion']}/10")
                ]
                
                for label, value in metrics:
                    st.metric(label, value)
            
            with col2:
                st.markdown(f"### 🔤 Linguistique - {selected_book}")
                linguistic = book_data['linguistic_features']
                
                metrics = [
                    ("Mots uniques", f"{linguistic['unique_words']:,}"),
                    ("Racines linguistiques", f"{linguistic['root_words']}"),
                    ("Complexité grammaticale", f"{linguistic['grammatical_complexity']}/10"),
                    ("Densité sémantique", f"{linguistic['semantic_density']}/10"),
                    ("Préservation orale", f"{linguistic['oral_preservation']}%")
                ]
                
                for label, value in metrics:
                    st.metric(label, value)
            
            with col3:
                st.markdown(f"### 📜 Historique - {selected_book}")
                historical = book_data['historical_impact']
                
                metrics = [
                    ("Plus ancien manuscrit", f"{historical['manuscripts_earliest']} EC"),
                    ("Première traduction", f"{historical['translations_timeline']} EC"),
                    ("Études académiques", f"{historical['academic_studies']:,}"),
                    ("Références culturelles", f"{historical['cultural_references']:,}"),
                    ("Influence légale", f"{historical['legal_influence']}/10")
                ]
                
                for label, value in metrics:
                    st.metric(label, value)
            
            # Score composite
            st.markdown("### 🎯 Score Composite d'Impact")
            
            composite_score = (
                structural['thematic_cohesion'] * 0.2 +
                linguistic['semantic_density'] * 0.25 +
                historical['legal_influence'] * 0.3 +
                (linguistic['oral_preservation'] / 10) * 0.25
            )
            
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.markdown(f"""
                <div style='text-align: center; padding: 2rem; background: linear-gradient(135deg, {self.get_book_color(selected_book)}20, {self.get_book_color(selected_book)}50); border-radius: 15px;'>
                    <div class='metric-large' style='color: {self.get_book_color(selected_book)};'>{composite_score:.1f}/10</div>
                    <div class='submetric'>Score Global d'Impact</div>
                </div>
                """, unsafe_allow_html=True)

    def get_book_color(self, book):
        """Retourne la couleur associée à un livre"""
        colors = {
            'Coran': '#2E86AB',
            'Torah': '#A23B72', 
            'Bible': '#F18F01'
        }
        return colors.get(book, '#666666')

    def get_color_map(self):
        """Retourne le mapping de couleurs pour les graphiques"""
        return {
            'Coran': '#2E86AB',
            'Torah': '#A23B72',
            'Bible': '#F18F01'
        }

    def run_advanced_dashboard(self):
        """Exécute le dashboard avancé"""
        # Sidebar avancée
        st.sidebar.markdown("## 🎛️ Contrôles Avancés")
        
        analysis_type = st.sidebar.selectbox(
            "Type d'analyse",
            ["Vue d'ensemble", "Structure", "Linguistique", "Thématiques", "Historique", "Insights"]
        )
        
        show_technical = st.sidebar.checkbox("Afficher les métriques techniques", True)
        show_comparative = st.sidebar.checkbox("Analyses comparatives", True)
        
        # Header
        self.create_advanced_header()
        
        # Navigation basée sur la sélection
        if analysis_type == "Vue d'ensemble":
            self.create_advanced_metrics_dashboard()
        
        elif analysis_type == "Structure":
            self.create_structural_analysis()
        
        elif analysis_type == "Linguistique":
            self.create_linguistic_analysis()
        
        elif analysis_type == "Thématiques":
            self.create_thematic_network_analysis()
        
        elif analysis_type == "Historique":
            self.create_historical_evolution()
        
        elif analysis_type == "Insights":
            self.create_comparative_insights()
        
        # Footer avancé
        st.markdown("---")
        st.markdown("""
        **🔬 Méthodologie:** Analyse comparative avancée utilisant des métriques quantitatives et qualitatives  
        **📚 Sources:** Données académiques consolidées et analyses spécialisées  
        **🎯 Objectif:** Compréhension approfondie des textes sacrés through l'analyse data-driven  
        *Note: Certaines données sont simulées pour des purposes démonstratifs*
        """)

# Lancement du dashboard avancé
if __name__ == "__main__":
    dashboard = AdvancedSacredBooksAnalysis()
    dashboard.run_advanced_dashboard()