// +++ App Bases
Table bases.base{
  id uuid [PK]
  created datetime [note:'auto_now_add']
  updated datetime [note:'auto_now']
}

// +++ App Accounts
Table accounts.user{
  id uuid [PK]
  email text [not null,unique]
  is_active bool [not null]
}

Table accounts.profile{
  id uuid [PK]
  user uuid [ref: - accounts.user.id]
  name text
  description text
  is_coordinator bool
  photo uuid [ref: < accounts.image.id]
  // offices uuid[] [ref: <> commons.office.id]
}

Table accounts.image{
  id uuid [PK]
  image text [not null]
  name text
  extension text
  size int
  deleted bool
  profile uuid [ref: < accounts.profile.id]
}

// +++ App Commons
// Table commons.office{
//   id uuid [PK]
//   name text [not null]
//   code text [not null]
// }

// +++ App musics
Table musics.album{
  id uuid [PK]
  name text
  description text
  image image [ref: < medias.image.id]
  listeners uuid[] [ref: <> accounts.profile.id]
  coordinator uuid [ref: < accounts.profile.id]
}

Table musics.sound{
  id uuid [PK]
  name text [not null]
  description text
  audio uuid [ref: < medias.audio.id]
  image image [ref: < medias.image.id]
  author uuid [ref: < accounts.profile.id]
  album uuid [ref: < musics.album.id]
}

// +++ App Medias
Table medias.audio{
  id uuid [PK]
  audio text [not null]
  description text
  extension text
  size int
  deleted bool
  profile uuid [ref: < accounts.profile.id]
}

Table medias.image{
  id uuid [PK]
  image text [not null]
  description text
  extension text
  size int
  deleted bool
  profile uuid [ref: < accounts.profile.id]
}